n = int(input())
(a, b) = (0, 0)
for i in range(n):
    (da, db) = map(int, input().split())
    a += da
    b += db
print(min(n - a, a) + min(n - b, b))
