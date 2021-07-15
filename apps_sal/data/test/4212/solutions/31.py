from itertools import combinations_with_replacement
n,m,q = list(map(int, input().split()))
abcd = [list(map(int, input().split())) for _ in range(q)]

ans = 0
for ary in combinations_with_replacement(range(1, m+1), n):
    p = 0
    for a,b,c,d in abcd:
        if ary[b-1] - ary[a-1] == c:
            p += d
    ans = max(ans, p)

print(ans)
