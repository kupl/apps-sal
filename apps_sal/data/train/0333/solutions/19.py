from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n_arr = len(arr)
        if n_arr <= 1:
            return 0
        
        value_arr_map = defaultdict(list)
        for i, n in enumerate(arr):
            value_arr_map[n].append(i)
        
        head = [0]
        tail = [n_arr-1]
        visited = {0, n_arr-1}
        n_move = 0
        while head or tail:            
            if len(head) > len(tail):
                head, tail = tail, head 
            
            next_head = []
            for current_index in head:
                current_value = arr[current_index]

                candidates = []
                if current_value in value_arr_map:
                    candidates += value_arr_map[current_value]            
                if current_index < n_arr - 1:
                    candidates += [current_index+1]
                if current_index > 0:
                    candidates += [current_index-1]
                for cand in candidates:
                    if cand in tail:
                        return n_move + 1
                    elif cand not in visited:
                        visited.add(cand)
                        next_head.append(cand)

            if current_value in value_arr_map:
                del value_arr_map[current_value]
            head = next_head                
            n_move += 1
        raise ValueError()
