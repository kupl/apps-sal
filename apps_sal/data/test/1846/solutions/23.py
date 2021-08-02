import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
r = sys.maxsize
t = list(map(int, input().split()))
l1 = [0] * (n + 1)
l2 = [0] * (n + 1)
for i, j in enumerate(t):
    l1[i + 1] = l1[i] + (0 if j < 0 else 1)
    l2[i + 1] = l2[i] + (0 if j > 0 else 1)
for k in range(1, n):
    r = min(r, l1[k] + l2[n] - l2[k])
print(r)
