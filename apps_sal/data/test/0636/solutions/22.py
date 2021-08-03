N, K = list(map(int, input().split()))
s = list(sorted([(int(n), i) for i, n in enumerate(input().split())]))

ans = []
n = 0
for c, i in s:
    if n + c > K:
        break
    ans.append(i + 1)
    n += c
print(len(ans))
if ans:
    print(' '.join(map(str, ans)))
