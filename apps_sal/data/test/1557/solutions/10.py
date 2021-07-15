def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

h1, a1, c1 = mi()
h2, a2 = mi()
ans = []
while h2 > 0:
    h1 -= a2
    if h1 > 0 or h2 <= a1:
        ans += ['STRIKE']
        h2 -= a1
    else:
        ans += ['HEAL']
        h1 += c1
print(len(ans))
print(*ans, sep='\n')
