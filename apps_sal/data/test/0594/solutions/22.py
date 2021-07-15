3

def readln(): return tuple(map(int, input().split()))

n, m = readln()
a = readln()
b = readln()
ans = -1
for v in range(max(a), min(b)):
    if [_ for _ in a if 2 * _ <= v]:
        ans = v
        break
print(ans)

