n = int(input())
l = [int(x) for x in input().split()]
found = False

if n < 4:
    print("no")
else:
    for i in range(n - 2):
        a = min(l[i], l[i + 1])
        b = max(l[i], l[i + 1])
        for j in range(i + 1, n - 1, 1):
            c = min(l[j], l[j + 1])
            d = max(l[j], l[j + 1])

            if c < a and a < d and b > d:
                found = True
                break
            if c < b and b < d and a < c:
                found = True
                break
        if found:
            break
    if found:
        print("yes")
    else:
        print("no")
