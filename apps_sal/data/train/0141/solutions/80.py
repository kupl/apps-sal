class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p1 = 0
        p2 = len(people) - 1
        count = 1
        cur = 0
        curNum = 0
        while p1 <= p2:
            if people[p2] <= limit - cur and curNum < 2:
                cur = cur + people[p2]
                curNum += 1
                p2 -= 1
                continue
            if people[p1] <= limit - cur and curNum < 2:
                cur = cur + people[p1]
                curNum += 1
                p1 += 1
                continue
            count += 1
            cur = 0
            curNum = 0

        return count
