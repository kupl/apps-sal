n = int(input())
listi = [int(x) for x in input().split()]
s = 0
m = max(listi)
for i in listi:
    s = s + (m - i)
print(s)
