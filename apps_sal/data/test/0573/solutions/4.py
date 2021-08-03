n = int(input())
s = input()
k = s.split()
m = k.count('1')
n = k.count('2')
if m <= n:
    total = m
else:
    total = n + (m - n) // 3
print(total)
