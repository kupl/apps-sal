class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats = people[:(1 + len(people)) // 2]
        onboard = [1] * len(boats)

        i = 0
        j = len(boats)
        k = len(people) - 1
        while j <= k:
            if i == len(boats):
                boats.append(people[j])
                j += 1
                if j > k:
                    break

            target = limit - boats[i]

            if people[k] > target:
                i += 1
                if i == len(boats):
                    boats.append(people[j])
                    j += 1
            else:
                boats[i] += people[k]
                k -= 1
                i += 1

        return len(boats)
