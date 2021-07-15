n = int(input())
A = sorted(map(int,input().split()))

if n % 2 == 1:
    ex = [0]
    
    for i in range(n//2):
        a = 2 * (i+1)
        ex += [a,a]
        
else:
    ex = []
    a = 1
    
    for i in range(n//2):
        ex += [a,a]
        a += 2
        
ans = 0

if A == ex:
    ans = 2 ** (n//2) % (10**9 + 7)
    
print(ans)
