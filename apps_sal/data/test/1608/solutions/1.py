import sys

mod = 10**9 + 7

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]

    cnt = [0]*(10**5 + 1)
    pat = [0]*(10**5 + 1)

    for ai in a:
        cnt[ai] += 1

    for i in range(1, 10**5 + 1):
        for j in range(2*i, 10**5 + 1, i):
            cnt[i] += cnt[j]
        
        pat[i] = (pow(2, cnt[i], mod) - 1)

    for i in range(10**5, 0, -1):
        for j in range(2*i, 10**5 + 1, i):
            pat[i] = (pat[i] - pat[j]) % mod

    ans = pat[1] % mod

    print(ans)

def __starting_point():
    solve()
__starting_point()
