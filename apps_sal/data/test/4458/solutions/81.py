from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    minimum = p[0]
    for i in range(1, n):
        if minimum >= p[i]:
            ans += 1
            minimum = p[i]
    print(ans)

main()
