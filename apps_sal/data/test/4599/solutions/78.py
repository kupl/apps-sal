n = int(input())
a = list(map(int, input().split()))
al = []
bb = []

a.sort(reverse=True)

for i in range(n):
    if i % 2 == 1:
        bb.append(a[i])
    else:
        al.append(a[i])

print((sum(al) - sum(bb)))
