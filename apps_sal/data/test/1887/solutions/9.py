n = int(input())

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))


m1 = [0] * n
m2 = [0] * n

m1[0] = a1[0]
m2[0] = a2[0]
if n != 1:
    m1[1] = m2[0] + a1[1]
    m2[1] = m1[0] + a2[1]

for i in range(2, n):
    m1[i] = max((m2[i - 1] + a1[i], m1[i - 2], m2[i - 2] + a1[i]))
    m2[i] = max((m1[i - 1] + a2[i], m2[i - 2], m1[i - 2] + a2[i]))

print(max(m1[-1], m2[-1]))
