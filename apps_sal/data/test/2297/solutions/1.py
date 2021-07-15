def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

for _ in range(ii()):
    l, r = mi()
    l -= 1
    sr = r // 2 + (r % 2) * -r
    sl = l // 2 + (l % 2) * -l
    print(sr - sl)
