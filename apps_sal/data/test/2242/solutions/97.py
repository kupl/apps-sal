import sys
readline = sys.stdin.readline

S = readline().rstrip()
DIV = 2019

cur = 0
from collections import defaultdict
dic = defaultdict(int)
for i in range(len(S) - 1, -1, -1):
  cur += ((int(S[i]) % DIV) * pow(10, (len(S) - 1 - i), DIV)) % DIV
  cur %= DIV
  dic[cur] += 1

ans = 0
# 0は単独でもよい
for key, val in dic.items():
  if key == 0:
    ans += val
  ans += (val * (val - 1)) // 2

print(ans)
