class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        numPeople = len(hats)
        hatDesired = defaultdict(set)
        MAX_HATS = 0
        BIG_NUMBER = 10**9 + 7
        for index, hatPreferences in enumerate(hats):
            for hat in hatPreferences:
                hatDesired[hat].add(index)
                MAX_HATS = max(MAX_HATS, hat)
        numberWays = defaultdict(int)

        def computeWays(assigned, currentHat):
            if (assigned, currentHat) in numberWays:
                return numberWays[(assigned, currentHat)]
            else:
                if currentHat == MAX_HATS + 1:
                    if sum(assigned) != numPeople:
                        answer = 0
                    else:
                        answer = 1
                else:
                    answer = 0
                    answer += computeWays(assigned, currentHat + 1)  # don't assign currentHat to anyone.
                    answer %= BIG_NUMBER
                    for index, num in enumerate(assigned):
                        if num == 0 and index in hatDesired[currentHat]:
                            nextList = list(assigned)
                            nextList[index] = 1
                            nextTuple = tuple(nextList)
                            answer += computeWays(nextTuple, currentHat + 1)
                            answer %= BIG_NUMBER
                numberWays[(assigned, currentHat)] = answer
                return answer
        return computeWays(tuple([0] * numPeople), 1)  # be careful about arguments you provide
