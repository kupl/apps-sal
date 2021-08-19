(g, b, c) = list(map(int, input().split()))
a = [g, b, c]
a.sort()
t = a[2] - a[0]
h = a[2] - a[1]
ans = t // 2 + h // 2
for i in range(3):
    a[i] = a[i] % 2
if a[0] == 0:
    if a[1] == 0:
        if a[2] == 0:
            print(ans)
        else:
            print(ans + 1)
    else:
        print(ans + 2)
elif a[1] == 0:
    print(ans + 2)
elif a[2] % 2 == 0:
    print(ans + 2)
else:
    print(ans)
