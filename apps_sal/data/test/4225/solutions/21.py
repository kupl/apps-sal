a, b, c, k = list(map(int, input().split()))
count = 0
if a >= k:
    count += min(a, k)
elif a + b >= k:
    count += a
else:
    count += (a - (k - a - b))
print(count)
