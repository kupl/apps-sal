n = int(input())
a = [*list(map(int, input().split()))]
b = sorted([(i, a[i]) for i in range(n)], key=lambda x: x[1])
current = 0
for i in b:
    if current < i[1]:
        current = i[1]
        a[i[0]] = str(a[i[0]])
    else:
        current += 1
        a[i[0]] = str(current)
print(" ".join(a))
