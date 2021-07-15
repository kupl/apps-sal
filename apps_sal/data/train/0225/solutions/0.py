INF = float('inf')
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        d1 = [-1] * n
        d2 = [-1] * n
        
        cnt = INF
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                cnt = 0
            elif dominoes[i] == '.':
                cnt += 1
            elif dominoes[i] == 'R':
                cnt = INF
            d1[i] = cnt
        
        cnt = INF
        for i in range(n):
            if dominoes[i] == 'R':
                cnt = 0
            elif dominoes[i] == '.':
                cnt += 1
            elif dominoes[i] == 'L':
                cnt = INF
            d2[i] = cnt
    
        ret = []
        for i in range(n):
            if d1[i] == d2[i]:
                ret.append('.')
            elif d1[i] < d2[i]:
                ret.append('L')
            else:
                ret.append('R')
        return ''.join(ret)
