n, k = list(map(int, input().split()))
a = 1
while n >= k ** a:
    a += 1
print(a)
