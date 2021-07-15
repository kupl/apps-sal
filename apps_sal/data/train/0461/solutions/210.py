class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        queue = collections.deque([(headID, 0)])
        subordinates = collections.defaultdict(list)
        
        for subordinate,supervisor in enumerate(manager):
            subordinates[supervisor].append(subordinate)

        time = 0
        
        while queue:
            supervisor,currentInformTime = queue.popleft()
            time = max(time,currentInformTime) # We are grabbing the maximum time over here 
            # because the boss might be connected to multiple subord. So whenever time is incremented we add it only once because in the queue we can have multiple subordinates from same boss with same times, so we wanna add it only once 
            
            for subordinate in subordinates[supervisor]:
                queue.append((subordinate,currentInformTime+informTime[supervisor]))
        
        return time   
    
# An alternate to line 13 would be to do xs.append(currentTime) and then on line 19 return max(xs)

