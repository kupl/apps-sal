class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if i > 8 else -1 for i in hours]
        hsh = {hours[0]:0}
        for i in range(1, len(hours)):
            hours[i] += hours[i-1]
            hsh[hours[i]] = i
            
        vals = [i+1 if hours[i] > 0 else 0 for i in range(len(hours))]
        for i in range(len(hours)):
            sm = hours[i] + 1
            if sm in hsh:
                v = hsh[sm]
                vals[v] = max(vals[v], v-i+vals[i])
                        
        return max(vals)
            

