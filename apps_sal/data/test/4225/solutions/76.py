a, b, c, k = map(int, input().split())
score = 0
remain = k

if a >= k:
    score = k
elif a < k and k <= a + b:
    score = a
else:
    score = a - (k - a - b)
print(score)
