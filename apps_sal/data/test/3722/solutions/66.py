from collections import defaultdict, Counter
mod = 10 ** 9 + 7
N = int(input())
aa, ab, ba, bb = input(), input(), input(), input()
dic = {}
dic['A', 'A'], dic['A', 'B'], dic['B', 'A'], dic['B', 'B'] = aa, ab, ba, bb
dp = {"AB"}
if N <= 3:
  print((1))
else:
  for _ in range(3):
    dp2 = set()
    for s in dp:
      for i, (a, b) in enumerate(zip(s, s[1:]), 1):
        dp2.add(s[: i] + dic[a, b] + s[i:])
    dp = dp2
  if len(dp) == 1:
    print((1))
  elif len(dp) == 3:
    x, y = 1, 1
    for _ in range(N - 3):
      x, y = y, (x + y) % mod
    print(y)
  else:
    print((pow(2, N - 3, mod)))

