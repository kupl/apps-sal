n = int(input())
Dup = []

for i in range(n):
    a = int(input())
    Dup.append([])
    for j in range(a):
        x,y = map(int, input().split())
        Dup[-1].append((x-1,y))

def is_honest (i,j):
    return (i >> j)%2 == 1

def honest_cnt(i):
    ans = 0
    for j in range(n):
        ans += is_honest(i,j)
    return ans

ans = 0

for i in range(1 << n):
    ok = True
    for j in range(n):
        if not is_honest(i,j):continue

        for x,y in Dup[j]:
            if y == 0 and is_honest(i,x): ok = False
            if y == 1 and not is_honest(i,x): ok = False

    if ok:
        ans = max(ans,honest_cnt(i))

print(ans)
