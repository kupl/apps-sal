n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
bc = []
for i in range(m):
    bc.append(list(map(int, input().split())))
bc.sort(key=lambda x: x[1], reverse=True)

for i in bc:
    if a[0] < i[1]:
        for j in range(i[0]):
            if a[0] < i[1]:
                a.append(i[1])
                del a[0]
            else:
                break
    else:
        break

print((sum(a)))
