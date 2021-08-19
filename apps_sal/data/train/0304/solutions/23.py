class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        ageIdx = defaultdict(list)
        for (i, age) in enumerate(ages):
            ageIdx[age].append(i)
        count = 0
        for age in ageIdx:
            lowerBound = int(1 / 2 * age) + 7 + 1
            upperBound = age
            for A in ageIdx[age]:
                for candAge in range(lowerBound, upperBound + 1):
                    if candAge in ageIdx:
                        if candAge != age:
                            count += len(ageIdx[candAge])
                        else:
                            count += len(ageIdx[candAge]) - 1
        return count
