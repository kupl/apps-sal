n = int(input())
d = [-1] * (2 * n)
ok = True
for _ in range(n):
    s, t = list(map(int, input().split()))
    s -= 1; t -= 1
    if s == t == -2:
        continue
    if (
      s >= 0 and d[s] != -1 or
      t >= 0 and d[t] != -1 or
      s >= 0 and t >= 0 and s >= t
    ):
        print('No')
        return
    if s == -2:
        d[t] = -2
    elif t == -2:
        d[s] = -3
    else:
        d[s] = t
        d[t] = s
dp = [[False] * (2 * n + 1) for _ in range(2 * n + 1)]
for w in range(2, 2 * n + 1, 2):
    for i in range(0, 2 * n - w + 1, 2):
        j = i + w
        k = i + w // 2
        if all(
          d[a] == -1 and (d[b] == -1 or d[b] == -2) or
          d[a] == -3 and d[b] == -1 or
          d[a] == b and d[b] == a
          for a, b in zip(list(range(i, k)), list(range(k, j)))
        ) or any(
            dp[i][k] and dp[k][j] for k in range(i+2, j, 2)
        ):
            dp[i][j] = True
print(('Yes' if dp[0][2 * n] else 'No'))

