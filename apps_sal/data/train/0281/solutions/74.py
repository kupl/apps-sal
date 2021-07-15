class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        shift_needed = collections.defaultdict(int)
        for sc, tc in zip(s, t):
            if sc > tc:
                shift_needed[ord('z')-ord(sc)+ord(tc)-ord('a')+1] += 1
            elif sc < tc:
                shift_needed[ord(tc)-ord(sc)] += 1
                
        min_move_needed = 0
        for shift, v in list(shift_needed.items()):
            min_move_needed = max(min_move_needed, 26*(v-1)+shift)
        #print(shift_needed, min_move_needed)
        return min_move_needed <= k

