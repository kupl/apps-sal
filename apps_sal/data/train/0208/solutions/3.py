class Solution:
     def predictPartyVictory(self, senate):
         """
         :type senate: str
         :rtype: str
         """
         queue = collections.deque()
         people, bans = [0, 0], [0, 0]
         
         for person in senate:
             x = person == 'R'
             people[x] += 1
             queue.append(x)
         
         while all(people):
             x = queue.popleft()
             if bans[x]:
                 bans[x] -= 1
                 people[x] -= 1
             else:
                 bans[x^1] += 1
                 queue.append(x)
         
         return 'Radiant' if people[1] else 'Dire'

