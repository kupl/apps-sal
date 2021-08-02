n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b)
for i in a:
    for j in b:
        if i == j:
            print(str(i))
            return

print(min(int(str(a[0]) + str(b[0])), int(str(b[0]) + str(a[0]))))
