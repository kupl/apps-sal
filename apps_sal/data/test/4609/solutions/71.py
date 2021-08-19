N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
ans = 0
prev = -1
cnt = 0
for a in A:
    if a == prev:
        cnt += 1
    else:
        ans += cnt % 2
        prev = a
        cnt = 1
else:
    ans += cnt % 2
print(ans)
