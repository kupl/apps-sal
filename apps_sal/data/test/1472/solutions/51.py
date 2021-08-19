(n, x, y) = map(int, input().split())
anslist = [0] * n
temp = 0
for i in range(1, n):
    for j in range(i + 1, n + 1):
        temp = min(abs(j - i), abs(x - i) + 1 + abs(y - j), abs(y - i) + 1 + abs(x - j))
        anslist[temp] += 1
anslist.pop(0)
for i in anslist:
    print(i)
