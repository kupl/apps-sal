n = int(input())
arr = list(map(int, input().split()))
r = n - arr[0]
p = 1
c = -1
for i in range(n):
    if p == 1:
        t = (arr[i] + r) % n        
    else:
        t = (n - (r - arr[i])) % n
    p = -p
    if t > c:
        c = t 
    else:
        print('No')
        break
else:
    print('Yes')
        

