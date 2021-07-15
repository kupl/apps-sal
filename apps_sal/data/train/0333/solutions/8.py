class Solution:
    def minJumps(self, arr: List[int]) -> int:
  
        
        
        val_to_ids = collections.defaultdict(list)
        _ = [val_to_ids[x].append(i) for i, x in enumerate(arr)]
        
        # print(val_to_ids)
        queue = collections.deque([(0, 0)])
        positions_seen = set()
        num_met = set()
        while queue:
            i, dis = queue.popleft()
            if i == len(arr) - 1:
                return dis
            val = arr[i]
            positions_seen.add(i)
            
            possible_indexes = []
            possible_indexes.append(i + 1)
            possible_indexes.append(i - 1)
            
            if len(val_to_ids[val]) > 1:
                for idx in val_to_ids[val]:
                    if idx not in positions_seen:
                        possible_indexes.append(idx)
                del val_to_ids[val]

            for p in possible_indexes:
                if p < 0 or p > len(arr) or p in positions_seen:
                    continue
                queue.append((p, dis+1))
            

        
#         nei = collections.defaultdict(list)
#         _ = [nei[x].append(i) for i, x in enumerate(arr)]

#         frontier = collections.deque([(0,0)])
#         num_met, pos_met = set(), set()
#         while frontier:
#             pos, step = frontier.popleft() # state: position, step
#             if pos == len(arr) - 1: return step
#             num = arr[pos]
#             pos_met.add(pos) # track explored positions

#             for p in [pos - 1, pos + 1] + nei[num] * (num not in num_met):
#                 if p in pos_met or not 0 <= p < len(arr): continue
#                 frontier.append((p, step + 1))

#             num_met.add(num) # track explored values

