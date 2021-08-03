a, b, k = map(int, input().split(" "))
if a < k:
    k -= a
    a = 0
    if b < k:
        b = 0
    else:
        b -= k
else:
    a -= k
print(a, b)
