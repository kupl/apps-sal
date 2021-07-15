def solve():
  n, k = map(int, input().split())
  p = [tuple(map(int, input().split())) for i in range(n)]
  p.sort()
  ans = 4000000000000000000
  for i in range(k, n + 1):
      for j in range(n - i + 1):
          x = p[i + j - 1][0] - p[j][0]
          s = [p[a][1] for a in range(j, i + j)]
          s.sort()
          y = 4000000000
          for a in range(i - k + 1):
            y = min(y, s[a + k - 1] - s[a])
          ans = min(ans, x * y)
  print(ans)
solve()
