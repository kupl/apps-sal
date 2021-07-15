3

def readln(): return tuple(map(int, input().split()))

n, k = readln()
ans = 0
for _ in range(n):
    v = set(map(int, list(input())))
    fl = True
    for i in range(k + 1):
        if i not in v:
            fl = False
    ans += fl
print(ans)

