a = [0] * 4
for i in range(4):
    s = input().strip()
    a[i] = len(s) - 2
ans = 'C'
f = 0
for i in range(4):
    f1 = 1
    f2 = 1
    for j in range(4):
        if i != j and a[i] < 2 * a[j]:
            f1 = 0
        if i != j and 2 * a[i] > a[j]:
            f2 = 0
    if f1:
        ans = chr(ord("A") + i)
        f += 1
    if f2:
        ans = chr(ord("A") + i)
        f += 1
if f == 1:
    print(ans)
else:
    print("C")
