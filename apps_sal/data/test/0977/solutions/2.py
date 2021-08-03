import bisect

n, p = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
ans = []
for x in range(0, 2001):
    temp = [i + x for i in range(n)]
    for j in range(n - 1, -1, -1):
        id = bisect.bisect_left(temp, a[j])
        num = 1 + j - id
        if num % p == 0 or num <= 0:
            break
    else:
        ans.append(x)

ans.sort()
print(len(ans))
print(*ans)
