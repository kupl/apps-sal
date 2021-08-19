n, k, c = list(map(int, input().split()))
s = input()

available = []
for i in range(n):
    if s[i] == "o":
        available.append(i)

# 左側から〇を数える
left = [0] * n
rest = 0
cnt = 0

for i in range(n):
    if s[i] == "o" and i >= rest:
        cnt += 1
        left[i] = cnt
        rest = i + c + 1
    else:
        left[i] = cnt

# 右側から〇を数える
right = [0] * n
rest = n - 1
cnt = 0

for i in range(n - 1, -1, -1):
    if s[i] == "o" and i <= rest:
        cnt += 1
        right[i] = cnt
        rest = i - c - 1
    else:
        right[i] = cnt

# -1日目、n+1日目がエラーにならないように0を足す
for i in ([left, right]):
    i.insert(0, 0)
    i.append(0)

ans = []

for i in range(1, n + 1):
    a = left[i - 1] + right[i + 1]
    if a < k:
        ans.append(i)

for j in ans:
    print(j)
