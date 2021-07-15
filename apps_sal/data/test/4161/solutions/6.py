from math import gcd
def main():
    ans = 0
    k = int(input())
    for i in range(1,1+k):
        for j in range(1,1+k):
            for l in range(1,1+k):
                ans += gcd(i,gcd(j,l))
    print(ans)


def __starting_point():
    main()
__starting_point()
