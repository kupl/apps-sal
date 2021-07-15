import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
t = list(map(int,sys.stdin.readline().split()))
p = [0] * 5001
for i in t:
    p[i] += 1
q = p[:]
for i in range(1, 5001):
    q[i] += q[i - 1]
ans = q[5000] - q[2499]
for i in range(1, 2501):
    if p[i]:
        s = q[2 * i] - q[i - 1]
        if s > ans: ans = s
print(n - ans)
