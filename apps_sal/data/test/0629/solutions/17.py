n = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
vert = list(map(int, input().split()))
lo = float('inf')
res = 0
firstcross = 0
secondcross = 0
for i in range(n):
    #print("i", i)
    cur = vert[i]
    cur += sum(row2[i:])
    cur += sum(row1[:i])
    # print(cur)
    if cur < lo:
        firstcross = i
        lo = cur
#print("cross", firstcross)
res += lo
lo = float('inf')
for i in range(n):
    #print("i", i)
    cur = vert[i]
    for j in range(i):
        #print("j row1", j)
        cur += row1[j]
    for j in range(i, n - 1):
        #print("j row2", j)
        cur += row2[j]
    # print(cur)
    if cur < lo and i != firstcross:
        lo = cur
        secondcross = i
#print("cross", secondcross)

res += lo
print(res)
