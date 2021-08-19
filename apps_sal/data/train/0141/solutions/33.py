class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        print(people)
        i = 0
        j = n - 1
        re = []
        c = 0
        tmp = []
        while i <= j:
            if people[i] + people[j] > limit:
                c += 1
                tmp.append(people[j])
                re.append(tmp)
                tmp = []
                j = j - 1
            else:
                tmp.append(people[i])
                tmp.append(people[j])
                re.append(tmp)
                tmp = []
                i = i + 1
                j = j - 1
        print(re)
        return len(re)
