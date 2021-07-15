import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():


    def prime_factor(n):
        lst = []
        while n%2 == 0:
            n //= 2
            lst.append(2)
        f = 3
        while f**2 <= n:
            if n%f == 0:
                n //= f
                lst.append(f)
            else:
                f += 2
        if n != 1:
            lst.append(n)
        return lst


    a, b = LI()
    g = math.gcd(a, b)

    prm = prime_factor(g)

    ans = len(set(prm)) + 1

    print(ans)

main()

