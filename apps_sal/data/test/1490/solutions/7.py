n, m = tuple(map(int, input().split()))
a = set(map(int, input().split()))
ans = []
for x in range(1, 10**9 + 1):
    if m < x:
        break
    if x not in a:
        ans.append(x)
        m -= x
print(len(ans))
print(" ".join(map(str, ans)))

