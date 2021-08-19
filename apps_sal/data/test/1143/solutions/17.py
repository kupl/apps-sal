import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
di = {}
k = 1
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(12):
    for j in range(days[i]):
        di[i + 1, j + 1] = k
        k += 1
n = int(input())
a = [0] * 512
for _ in range(n):
    (m, d, p, t) = map(int, input().split())
    temp = di[m, d]
    for x in range(temp - t, temp):
        a[x] += p
print(max(a))
