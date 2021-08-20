n = int(input())
ans = 10 ** 18
val = -1
arr = list(map(int, input().split()))
for i in range(1, 102):
    valx = 0
    for j in arr:
        if abs(j - i) > 1:
            valx += abs(j - i) - 1
    if valx < ans:
        ans = valx
        val = i
print(val, ans)
