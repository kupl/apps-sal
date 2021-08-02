def solve():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    i = 1
    while i <= N:
        if i == P[i - 1]:
            ans += 1
            i += 1
        i += 1
    return ans


print(solve())
