import sys
def main():
    a,b,c,d,e,f = list(map(int, sys.stdin.read().split()))
    ans = 0

    for i in range(0, d+1):
        t1 = min(a, i)
        t2 = min(b, c, d-i)

        if ans < t1 * e + t2 * f:
            ans = t1 * e + t2 * f

    print(ans)

main()

