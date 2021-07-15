import sys
stdin = sys.stdin
def main():
    N = int(stdin.readline().rstrip())
    A = list(map(int,stdin.readline().split()))
    mod = 10**9+7
    ans = 0
    for i in range(61):
        bits = 0
        for x in A:
            if (x>>i)&1:
                bits += 1
        ans += ((bits*(N-bits))* 2**i) %mod
    ans %= mod
    print(ans)
main()
