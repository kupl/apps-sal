n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    a[i] %= 2
    if len(b) != 0:
        if b[-1] == a[i]:
            b.pop()
        else:
            b.append(a[i])
    else:
        b.append(a[i])
if len(b) > 1:
    print("NO")
else:
    print("YES")

