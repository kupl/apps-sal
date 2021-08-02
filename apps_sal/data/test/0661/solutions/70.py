m, k = map(int, input().split())
if m * k == 1:
    print(-1)
    return

if k == 0:
    ans = []
    for i in range(2**m):
        ans.append(i)
        ans.append(i)
    print(*ans)
    return

if 2**m <= k:
    print(-1)
else:
    ans = [k]
    chk = list(range(2**m))
    chk.remove(k)
    ans = ans + chk + [k] + chk[::-1]
    print(' '.join(map(str, ans)))
