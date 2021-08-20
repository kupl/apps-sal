def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    idx = arr.index(n)
    ok = 1
    for i in range(1, idx):
        if arr[i] < arr[i - 1]:
            ok = 0
    for i in reversed(range(idx, n - 1)):
        if arr[i] < arr[i + 1]:
            ok = 0
    if ok:
        print('YES')
    else:
        print('NO')
    return 0


main()
