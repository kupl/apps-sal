n = int(input())
l = [int(i) for i in input().split()]

c = [0 for i in range(1000 + 1)]
k = []
for e in l[::-1]:
    if c[e] == 0:
        k.append(e)
        c[e] = 1

print(len(k))
for e in k[::-1]:
    print(e, end=" ")
print()
