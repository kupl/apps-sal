from collections import deque


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = deque(sorted(people))
        count = 0
        while len(people) > 1:
            lightest = people.popleft()
            heaviest = people.pop()
            if lightest + heaviest <= limit:
                count += 1
                continue
            else:
                if lightest < limit:
                    people.appendleft(lightest)
                else:
                    count += 1
                count += 1
        return count + len(people)
