n,h = map(int,input().split())
a = 0
b = []

for i in range(n):
    A,B = map(int,input().split())
    a = max(A,a)
    b.append(B)
    
b = sorted(b)[::-1]

for i in range(n):
    if 0 < h and a < b[i]:
        h -= b[i]
        ans = i + 1
        
    else:
        ans = i
        break
        
if 0 < h:
    ans += -(-h//a)
    
print(ans)
