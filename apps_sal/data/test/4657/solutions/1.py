def main():
    import sys
    input = sys.stdin.readline

    def solve():
        (n, k) = map(int, input().split())
        arr = list(map(int, input().split()))
        curr = 0
        ans = []
        for i in range(n):
            curr += arr[i]
            if curr & 1:
                curr = 0
                ans.append(i + 1)
        if len(ans) < k or len(ans) - k & 1:
            print('NO')
        else:
            print('YES')
            print(*ans[:k - 1] + [n])
    for _ in range(int(input())):
        solve()
    return 0


main()
