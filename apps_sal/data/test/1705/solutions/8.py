n = int(input())
arr = list(map(int, input().split()))

a = -1
b = -1
for x in range(n):
    if arr[x] == 0:
        a = x
    else:
        b = x
print(min(a, b) + 1)
