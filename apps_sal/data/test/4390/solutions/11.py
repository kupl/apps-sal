#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

# MOD = 998244353
# def pow(base , exp):
#     if exp == -1:
#         return pow(base , MOD - 2)
#     res = 1
#     base %= MOD
#     while exp > 0:
#         if exp % 2:
#             res = (res * base) % MOD
#         exp //= 2
#         base = (base * base) % MOD
    
#     res %= MOD
    #   return res

def main():
    t = int(input())
    for _ in range(t):
        a , b = map(int , input().split())
        if a % b == 0:
            print(0)
        else:
            print(b - a%b)
    return

def __starting_point():
    main()
__starting_point()
