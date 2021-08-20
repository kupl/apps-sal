n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
ans = -1
memo = 0
light = 1
for i in range(n):
    if light == 2:
        ans = memo
        break
    light = a[light - 1]
    memo += 1
print(ans)
