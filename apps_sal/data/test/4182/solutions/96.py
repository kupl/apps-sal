(n, m, x, y) = map(int, input().split())
(a, b) = [list(map(int, input().split())) for i in range(2)]
for i in range(x + 1, y + 1):
    if all((j < i for j in a)) and all((k >= i for k in b)):
        print('No War')
        break
else:
    print('War')
