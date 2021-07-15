MOD = pow(10,9)+7
def MODINV(n:int, MOD=MOD):
    return pow(n, MOD-2, MOD)

def main():
    N = int(input())
    ans = 1
    for i in range(N):
        ans *= i+1
        ans %= MOD
    print(ans)

def __starting_point():
    main()

__starting_point()
