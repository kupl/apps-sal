n = int(input())
seat = [0] * 10 ** 6
for i in range(n):
    (l, r) = list(map(int, input().split()))
    for j in range(l, r + 1):
        seat[j - 1] = 1
res = 0
for i in range(10 ** 6):
    if seat[i] == 1:
        res += 1
print(res)
