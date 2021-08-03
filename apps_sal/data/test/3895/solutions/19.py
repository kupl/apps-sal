n = int(input())
l = list(map(int, input().split()))
a = [0] * n
b = []
c = []
ptr = 1
for i in range(n):
    if(a[l[i] - 1] == 0):
        c.append(l[i])
        a[l[i] - 1] = ptr
        ptr += 1
    b.append(a[l[i] - 1])
for i in range(n):
    if(c[b[i] - 1] != l[i]):
        print(-1)
        return
for i in range(ptr - 1):
    if(b[c[i] - 1] - 1 != i):
        print(-1)
        return


print(ptr - 1)
for i in b:
    print(i, end=" ")
print()
for i in c:
    print(i, end=" ")
