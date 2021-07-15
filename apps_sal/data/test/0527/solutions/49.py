def solve():
  s = input()
  t = input()
  ans = 0
  alp = [[] for _ in range(27)]
  length_s = len(s)
  for i in range(length_s):
    char = ord(s[i]) - ord('a')
    alp[char].append(i + 1)
  length_t = len(t)
  import bisect
  for i in range(length_t):
    char = ord(t[i]) - ord('a')
    if alp[char]:
      if ans % length_s >= alp[char][-1]:
        ans = (ans // length_s + 1) * length_s
      index = bisect.bisect_right(alp[char], ans % length_s)
      ans += alp[char][index] - ans % length_s
    else:
      return -1
  return ans
print(solve())
