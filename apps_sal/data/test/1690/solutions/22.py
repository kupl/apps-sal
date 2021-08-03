n = int(input())
a = list(map(int, input().split()))

a = a[::-1]

k = 0
mx = a[0] + 2

for c in a:
    mx = max(0, mx - 1)
    #print(k, c, mx)
    if c < mx:
        k += c
        mx = c

    elif mx == c:
        k += max(c, 0)
        mx = max(c, 0)

    else:
        k += mx

print(k)
