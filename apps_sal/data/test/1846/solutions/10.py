import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
y = 0
ans = 10**9
l = [int(i) for i in input().split()]
x = sum(i <= 0 for i in l)
for i in range(n):
    if l[i] <= 0:
        x -= 1
    if l[i] >= 0:
        y += 1
    if i == n - 1 and l[i] <= 0:
        x += 1
    ans = min(ans, x + y)

print(ans)
