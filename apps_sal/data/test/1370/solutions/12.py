def main():
  from collections import Counter
  from collections import defaultdict
  from collections import deque
  from itertools import accumulate
  from itertools import combinations
  from itertools import permutations
  from itertools import product
  import sys
  sys.setrecursionlimit(10**6)
  readline = sys.stdin.readline
  ints = lambda: map(int, readline().split())
  floats = lambda: map(float, readline().split())
  lli = lambda I, J: [[0] * J for _ in range(I)]
  mod = 10**9+7

  h, w, k = ints()
  ans = h + w
  s = [list(map(int, input())) for _ in range(h)]
  for comb in product([False, True], repeat=h - 1):
    divs = 0
    a = [s[0][:]]
    for row, isd in zip(s[1:], comb):
      if isd:
        a += [row[:]]
        divs += 1
      else:
        for i in range(w):
          a[divs][i] += row[i]
    dh = divs + 1
    ta = [list(i) for i in zip(*a)]
    currow = ta[0]
    imp = False
    for row in ta[1:]:
      if any([i > k for i in currow]):
        imp = True
        break
      else:
        temp = [i + j for i, j in zip(currow, row)]
        if any([i > k for i in temp]):
          currow = row
          divs += 1
        else:
          currow = temp
    if not imp:
      ans = min(ans, divs)
  print(ans)

def __starting_point():
  main()
__starting_point()
