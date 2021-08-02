n = int(input())
x = list(input())
a = (n - 11 + 1) // 2
b = (n - 11) // 2
for i, ch in enumerate(x):
    if ch == '8':
        if b > 0:
            b -= 1
            x[i] = None
    else:
        if a > 0:
            a -= 1
            x[i] = None
for c in x:
    if c != None:
        if c != '8':
            print("NO")
        else:
            print("YES")
        break
