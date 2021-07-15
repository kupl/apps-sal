class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        moment_count = 0
        lit_idx = -1
        
        idx_map = {}
        
        for idx, moment in enumerate(light):
            idx_map[moment] = idx
            
        for moment in range(1, len(light) + 1):
            idx = idx_map[moment]
            light[idx] = 'L'
            
            if idx == lit_idx + 1:
                for l_idx in range(lit_idx + 1, len(light)):
                    if light[l_idx] == 'L':
                        lit_idx += 1
                    else:
                        break
                        
            if lit_idx + 1 == moment:
                moment_count += 1
        
        return moment_count
