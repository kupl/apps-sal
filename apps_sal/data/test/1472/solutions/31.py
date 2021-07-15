n, x, y = map(int, input().split())
li = [0] * (n - 1)
num = 0

for i in range(1, n):
    for j in range(i + 1, n + 1):
        num = min(j-i, abs(i-x)+abs(j-y)+1)
        li[num - 1] += 1

for i in li:
    print(i)
