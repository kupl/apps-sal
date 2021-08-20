N = int(input())
A = list(map(int, input().split()))
ans = 0
A.sort()
count = 0
m = 0
for i in range(N):
    if count == 0:
        m = A[i]
        count += 1
    elif A[i] == m:
        count += 1
    else:
        if m > count:
            ans += count
        else:
            ans += count - m
        count = 1
        m = A[i]
if m > count:
    ans += count
else:
    ans += count - m
print(ans)
