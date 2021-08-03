n, m, x, y = map(int, input().split())
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))
z = 'War'
for i in range(x + 1, y + 1):
    if max(xl) < i and i <= min(yl):
        z = 'No War'
        break
print(z)
