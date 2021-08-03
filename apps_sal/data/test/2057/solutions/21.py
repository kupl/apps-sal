n = int(input())
a = list(map(int, input().split()))
mn = set()
mn.add(0)
k = 1
for i in range(n):
    if a[i] in mn:
        mn -= {a[i]}
        mn.add(i + 1)
    else:
        k += 1
        mn.add(i + 1)
print(k)
