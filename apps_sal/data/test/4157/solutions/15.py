n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
    for k in a:
        if k*2 in a or k // 3 in a and k % 3 == 0:
             pass
        else:
            a.remove(k)
            b.append(k)
print(*reversed(b))


