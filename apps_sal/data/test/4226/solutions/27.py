x, y = map(int, input().split())
ans = 0
for i in range(x+1):
    if 2 * i + 4*(x-i) == y:
        ans = 1

print('Yes' if ans == 1 else 'No')
