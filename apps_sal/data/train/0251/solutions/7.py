class Solution:
    def clumsy(self, N: int) -> int:
        op = 0
        s = N
        N = N - 1
        sum_list = []
        sign_list = [1]
        
        while N > 0:
            if op == 0:
                s = s * N
            elif op == 1:
                s = s // N
            elif op == 2:
                sum_list.append(s)
                sign_list.append(1)
                s = N
            else:
                sum_list.append(s)
                sign_list.append(-1)
                s = N
            
            op = (op + 1) % 4
            N -= 1
            
        sum_list.append(s)
        
        s = 0
        for i, v in enumerate(sign_list):
            s+= sign_list[i] * sum_list[i]

        return s
                
            

