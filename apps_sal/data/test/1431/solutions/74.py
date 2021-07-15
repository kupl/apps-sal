def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*(n+1)
    ans = []
    for i in range(n, 0, -1):
        if sum(b[i::i])%2 != a[i-1]:
            ans.append(i)
            b[i] = (b[i]+1)%2
    print(len(ans))
    if len(ans):
        print(*reversed(ans))

def __starting_point():
    main()
__starting_point()
