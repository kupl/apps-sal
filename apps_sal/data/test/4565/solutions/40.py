n = int(input())
s = input()

left = [0] * n
right = [0] * n

tmp = 0
for i in range(1, n):
    if s[i - 1] == "W":
        tmp += 1
        left[i] = tmp
    else:
        left[i] = tmp

tmp = 0
for i in range(n - 2, -1, -1):
    if s[i + 1] == "E":
        tmp += 1
        right[i] = tmp
    else:
        right[i] = tmp

res = 10**9
for i in range(n):
    res = min(res, left[i] + right[i])
print(res)
