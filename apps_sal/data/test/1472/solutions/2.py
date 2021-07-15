def main():
    n, x, y = list(map(int, input().split()))
    ans = [0]*(n)
    for i in range(1, n):
        for j in range(i+1, n+1):
            ans[min(j-i, abs(x-i)+abs(y-j)+1)] += 1
    for v in ans[1:]:
        print(v)

def __starting_point():
    main()

__starting_point()
