class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        step = defaultdict(lambda : None)
        
        @lru_cache(None)
        def cal(i, j):
            if i >= len(str1):
                return len(str2)-j
            if j >= len(str2):
                return len(str1)-i
            
            if str1[i] == str2[j]:
                step[(i, j)] = 0
                return 1 + cal(i+1, j+1)
            else:
                a = cal(i+1, j)
                b = cal(i, j+1)
                if a < b:
                    step[(i, j)] = 1
                    return 1 + a
                else:
                    step[(i, j)] = 2
                    return 1 + b
        cal(0, 0)
        
        ans = []
        
        def cons(i, j):
            nonlocal ans  
            if i>=len(str1):
                ans.append(str2[j:])
                return 
            if j>=len(str2):
                ans.append(str1[i:])
                return
            s = step[(i, j)]
            if s == 0:
                ans.append(str1[i])
                i+=1
                j+=1
            elif s == 1:
                ans.append(str1[i])
                i+=1
            else:
                ans.append(str2[j])
                j+=1
            cons(i, j)
        cons(0, 0)
        return ''.join(ans)
