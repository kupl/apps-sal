n = int(input())
i = 0
true = 0
while i < n:
    (a, b) = list(map(int, input().split()))
    c = b - a
    if c >= 2:
        true += 1
    i += 1
print(true)
