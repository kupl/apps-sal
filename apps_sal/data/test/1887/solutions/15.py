n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
m1, m2 = 0, 0
for i in range(n - 1, -1, -1):
    x1, x2 = l1[i] + m2, l2[i] + m1
    if x1 > m1:
        m1 = x1
    if x2 > m2:
        m2 = x2
print(max(m1, m2))
