(r, g, b) = map(int, input().split(' '))
s = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if r >= i and g >= j and (b >= k):
                s = max(s, (r - i) // 3 + (g - j) // 3 + (b - k) // 3 + min(i, min(j, k)))
print(s)
