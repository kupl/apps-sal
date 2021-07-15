class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if len(s) != len(t):
            return False
        
        
        shift_times = []
        for idx in range(len(s)):
            a = s[idx]
            b = t[idx]
            if ord(a) <= ord(b):
                shift_times.append(ord(b) - ord(a))
            else:
                shift_times.append( (ord('z')-ord(a))+(ord(b)-ord('a')) + 1 )
            #print(shift_times, b, a, (ord('z')-ord(b)), (ord(a)-ord('a')))
            ## pruning for unable to shift
            if shift_times[-1] > k:
                return False
        

        shift_used = dict()
        for idx in range(len(shift_times)):
            shift_amount = shift_times[idx]
            if shift_amount == 0:
                continue
            ## shift_times already used before, should plus wrapping
            if shift_amount in shift_used:
                if 26 * shift_used[shift_amount] + shift_amount > k:
                    return False
                else:
                    shift_used[shift_amount] += 1
            ## can shift normally
            else:
                shift_used[shift_amount] = 1
        return True
        

