n = int(input())
d = dict()
for i in range(n):
    S = ''.join(sorted(list(input())))
    if S in d.keys():
        d[S] += 1
    else:
        d[S] = 1

ans = 0
for i in d.values():
    ans += i * (i - 1) // 2
print(ans)
