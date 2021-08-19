(n, m) = [int(v) for v in input().split()]
a = [int(v) - 1 for v in input().split()]
cnt = [0] * n
nonzero = 0
ans = []
for ai in a:
    cnt[ai] += 1
    if cnt[ai] == 1:
        nonzero += 1
        if nonzero == n:
            nonzero = 0
            for i in range(n):
                cnt[i] -= 1
                if cnt[i]:
                    nonzero += 1
            ans.append(True)
            continue
    ans.append(False)
print(''.join(('01'[v] for v in ans)))
