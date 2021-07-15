n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

i =0
j =0
ans = 0
sa = 0
sb = 0
while i < n or j < m:
    if sa < sb:
        if i>= n:
            break
        sa += A[i]
        i += 1
    else:
        if j >= m:
            break
        sb += B[j]
        j += 1
    if sa == sb:
        ans += 1
        sa = 0
        sb = 0

if i == n and j == m and sa == 0 and sb == 0: 
    print(ans)
else:
    print(-1)

