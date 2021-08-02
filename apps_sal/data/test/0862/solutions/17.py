n = int(input())
a = list(map(int, input().split()))
s = min(a)
for q in range(n):
    a[q] -= s // n * n
q1 = 0
while a[q1 % n] - q1 > 0:
    q1 += 1
print(q1 % n + 1)
