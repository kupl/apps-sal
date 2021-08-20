n = int(input())
s = 0
for i in range(n):
    (a, u) = input().split()
    if u == 'JPY':
        s += int(a)
    else:
        s += float(a) * 380000
print(s)
