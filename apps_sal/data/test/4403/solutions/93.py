import sys

S = sys.stdin.readline().strip()
ans = 0
for s_i in S:
    if s_i == "+":
        ans += 1
    else:
        ans -= 1
print(ans)
