(a, b, c) = list(map(int, input().split()))
count = b // a
if count > c:
    count = c
print(count)
