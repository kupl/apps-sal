# 

def update(t, l, ans):
    if l < ans[1]:
        ans[0] = t
        ans[1] = l
    
def solve():
    S, E, L = list(map(int, input().split()))
    
    n       = int(input())
    if n == 0:
        return S
    
    a       = list(map(int, input().split()))[::-1]

    if S < a[-1]:
        return S
    
    ans = [0, S]
    cur_t = S
    
    while cur_t+L <= E and len(a) > 0:
        if cur_t < a[-1]:
            return cur_t
        
        t  = a.pop()
        update(t-1, cur_t-t+1, ans)
        cur_t+=L    
    
    if cur_t+L <= E:
        return cur_t
    
    return ans[0]

print(solve())        
#10 15 2
#2
#10 13    

#8 17 3
#4
#3 4 5 8

