import sys

S = sys.stdin.readline().strip()
K = int(sys.stdin.readline())

for s_i in S:
    if s_i == "1":
        K -= 1
    else:
        break
    if K <= 0:
        break
print(s_i)
