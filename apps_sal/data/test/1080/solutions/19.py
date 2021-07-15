n = int(input())
b = list(map(int, input().strip().split()))
m = 0
s = 0
can = True
for i in b:
    m = max(m,i)
    s += i
if s%2:
    can = False
if 2*m > s:
    can = False
if can:
    print ('YES')
else:
    print ('NO')
