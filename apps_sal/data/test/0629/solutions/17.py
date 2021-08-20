n = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
vert = list(map(int, input().split()))
lo = float('inf')
res = 0
firstcross = 0
secondcross = 0
for i in range(n):
    cur = vert[i]
    cur += sum(row2[i:])
    cur += sum(row1[:i])
    if cur < lo:
        firstcross = i
        lo = cur
res += lo
lo = float('inf')
for i in range(n):
    cur = vert[i]
    for j in range(i):
        cur += row1[j]
    for j in range(i, n - 1):
        cur += row2[j]
    if cur < lo and i != firstcross:
        lo = cur
        secondcross = i
res += lo
print(res)
