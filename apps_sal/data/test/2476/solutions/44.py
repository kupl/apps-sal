from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

lst = [0] * (N)
for a in A:
    lst[a - 1] += 1
lst.sort()

s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + lst[i]


ans = N
i = N
for k in range(1, N + 1):
    while True:
        while i >= 1 and lst[i - 1] >= ans:
            i -= 1
        total = ans * (N - i) + s[i]
        if total >= ans * k:
            break
        ans -= 1
    print(ans)
