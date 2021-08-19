# cook your dish here
n, q = list(map(int, (input()).split()))
a = list(map(int, (input()).split()))
l = []
for j in range(1, max(a) + 1):
    if min(a) <= j and j <= max(a):
        l.append(j)
for i in range(q):
    t = int(input())
    if t in l:
        print("Yes")
    else:
        print("No")
