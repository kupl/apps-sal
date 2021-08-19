(w, h, k) = list(map(int, input().split()))
res = 0
for i in range(k):
    res += w * 2 + h * 2 - 4
    w -= 4
    h -= 4
print(res)
