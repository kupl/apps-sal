l, r, a = list(map(int, input().split()))

while a > 0:
    if l < r:
        l += 1
    elif r < l:
        r += 1
    else:
        l += 1
    a -= 1

print(2*min(l, r))

