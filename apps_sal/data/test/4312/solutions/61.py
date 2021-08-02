a, b, c, d = list(map(int, input().split()))
while a > 0:
    c = c - b
    if c > 0:
        a = a - d
    else:
        print("Yes")
        break
if c > 0:
    print("No")
