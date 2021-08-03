N = int(input())

num = set()
for n in range(2, 10**7):
    if N % n == 0:
        num.add(tuple(sorted([n, N // n])))
    if N == n:
        break
ans = (10**12, 10**12)
if not num:
    print(N - 1)
else:
    for s in num:
        if s[0] + s[1] < ans[0] + ans[1]:
            ans = s
    print(ans[0] + ans[1] - 2)
