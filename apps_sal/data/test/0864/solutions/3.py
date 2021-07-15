n, m = list(map(int, input().split()))
a = [0] * 100
inp = list(map(int, input().split()))

for i in inp:
    a[i - 1] += 1
    
go = True
ans = 0
for i in range(1000):
    
    b = [i for i in a]
    
    cnt = 0
    for j in b:
        cnt += j // (i + 1)
        
    go = cnt >= n
    
    if not go:
        ans = i
        break
print(i)

