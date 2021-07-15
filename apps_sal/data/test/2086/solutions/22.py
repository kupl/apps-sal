# Q.C
n = int(input())
a = input().split(" ")
a = list(map(int,a))
s,f = list(map(int, input().split(" ")))
a.insert(0,0)

x = 1
xm = x
li = s-x+1
ri = f-x
totalm = sum(a[i] for i in range(li,ri+1))
total = totalm

for x in range(2, n+1):
    li -= 1
    if li == 0:
        li = n
    total += a[li]
    total -= a[ri]
    ri -= 1
    if ri == 0:
        ri = n
    if total > totalm:
        totalm = total
        xm = x
print(xm)
