n, m  = [int(el) for el in input().split()]
for i in range(m):
    l, r = [int(el) for el in input().split()]
s = '01' * (n//2)
if n % 2 == 1:
    s += '0'
print(s)

