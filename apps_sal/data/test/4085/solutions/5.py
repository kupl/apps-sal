def divisors(n):
    res = set()

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n//i)
    
    return res

def solve():
    for _ in range(int(input())):
        N = int(input())
        D = set([int(k) for k in input().split()])
        
        ans = max(D) * min(D)
        
        if divisors(ans) != D:
            print(-1)
            continue
            
        print (ans)
    
def __starting_point():  
    solve() 

__starting_point()
