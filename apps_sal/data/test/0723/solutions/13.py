import sys

input = sys.stdin.readline


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans=float('inf')
    for i in range(1,1001):
        f=1
        curr=0
        for j in a:
            if j[0]>i and j[1]>i:
                f=0
                break
            else:
                if j[0] <= i and j[1] <= i:
                    curr+=min(j[0], j[1])
                else:
                    curr+=max(j[0], j[1])
        if f:
            #print(i,curr)
            ans=min(ans, curr*i)
    print(ans)

    return


def __starting_point():
    main()
__starting_point()
