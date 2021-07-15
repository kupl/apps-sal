k, x = map(int, input().split())
stone = []
for i in range(x-(k-1), x + (k)):
    stone.append(i)
print(*stone)
