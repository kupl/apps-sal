__author__ = 'Ol4a'
(m, d) = list(map(int, input().split()))
k = m + d - 1
print(k)
for i in range(1, d + 1):
    print(1, i)
for j in range(2, m + 1):
    print(j, 1)
