import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))
def fde(): print("-flag-")

def divisors(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n//i)

    return res


def main():
    N=ii()
    A=list(mi())
    R = divisors(A[0]) + divisors(A[1])

    ans = 0
    for r in R:
        miss_count = 0
        for a in A:
            if a % r != 0:
                miss_count += 1
                if miss_count == 2:
                    break
        
        if miss_count <= 1:
            ans = max(ans,r)
            

    print(ans)








def __starting_point():
    main()
__starting_point()
