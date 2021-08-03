n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
s1 = 0
s2 = 0
for i in range(n):
    s1 |= a[i]
    s2 |= b[i]
print(s1 + s2)
