n,p = map(int,input().split())
s = list(map(int, list(input())))

def solve():
    total = 0

    if 10%p == 0:
        for i in range(n):
            if s[i] % p == 0: total += i + 1
        return total

    cnt = [0]*p
    r = 0
    ten = 1
    for i in range(n-1, 0-1, -1):
        cnt[r] += 1
        r = (r + s[i]*ten) % p
        total += cnt[r]
        ten = ten * 10 % p
    return total

print(solve())
