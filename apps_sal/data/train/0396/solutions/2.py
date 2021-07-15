class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 0:
            return -1
        
        mod_group = 0
        n = '1'
        prev_modulo = {}
        
        while True:
            mod_group += 1
            if mod_group * 10 < K:
                mod_group *= 10
                n += '1'
                continue
            elif mod_group == K:
                return len(n)
                
            modulo = (mod_group * 10) % K
            if modulo in prev_modulo:
                return -1
            elif modulo + 1 == K:
                return len(n + '1')
                
            mod_group = modulo
            prev_modulo[modulo] = ''
            n += '1'
