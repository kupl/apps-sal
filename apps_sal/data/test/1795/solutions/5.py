n = int(input())
a = [int(z) for z in input().split()]
a = [0] + a
for i in range(1, n):
    if (a[a[a[i]]] == i):
        print("YES")
        return
print("NO")
