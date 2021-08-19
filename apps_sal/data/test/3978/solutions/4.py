def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    color = [0] * n
    arr.sort()
    ans = 0
    for i in range(n):
        if color[i]:
            continue
        ans += 1
        for j in range(i, n):
            if arr[j] % arr[i] == 0:
                color[j] = ans
    print(ans)
    return 0


main()
