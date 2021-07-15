n = int(input())
arr = list(map(int, input().split()))
b = c = 0
for val in arr:
    if val >= 0:
        b += val
    else:
        c += val
print(b - c)
