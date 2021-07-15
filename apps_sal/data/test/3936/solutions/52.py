N = int(input())
grid = [input(),input()]
MOD = 10**9 + 7

cnt = 3 if grid[0][0] == grid[1][0] else 6

for i in range(1,N):
    a,b = grid[0][i-1],grid[1][i-1]
    c,d = grid[0][i],grid[1][i]

    if a == b:
        cnt *= 2
    elif c != d and a != c:
        cnt *= 3
    cnt %= MOD

print(cnt)
