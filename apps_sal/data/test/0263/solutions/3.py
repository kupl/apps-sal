n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(int(input()))
mxa = max(a)
rmx = mxa + m
for x in a:
    m -= mxa - x
rmn = mxa
if m > 0:
    rmn += (m + n - 1) // n
print(rmn, rmx)
