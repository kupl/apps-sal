import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

ans = min(data[-1] - 1, 1000000 - data[0])
for i in range(n - 1):
    cur_ans = max(data[i] - 1, 1000000 - data[i + 1])
    ans = min(ans, cur_ans)
print(ans)

