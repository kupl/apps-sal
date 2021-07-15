class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        W = k
        hand = nums
        
        hand.sort()
        mp = defaultdict(list)
        
        for elem in hand:
            prev_len = -1 if len(mp[elem - 1]) == 0 else heapq.heappop(mp[elem - 1])
            if prev_len == -1 or prev_len == W:
                heapq.heappush(mp[elem], 1)
            else:
                heapq.heappush(mp[elem], prev_len + 1)
                
        for key in mp.keys():
            for length in mp[key]:
                if length != W:
                    return False
                
        return True
