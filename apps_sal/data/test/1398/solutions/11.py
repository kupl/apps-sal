import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', '+w')
n = int(input())
a = [0] + sorted(list(map(int, input().split())))
start = 1
res = 0
for end in range(1, n + 1):
    while a[end] > 2 * a[start]:
        start += 1
    res = max(res, end - start + 1)
print(n - res)
