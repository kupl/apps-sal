def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    s = arr[0]
    su = sum(arr)
    cnt = arr[0]
    ad = [1]
    for i in range(1, n):
        if s >= 2 * arr[i]:
            ad.append(i + 1)
            cnt += arr[i]
    if cnt * 2 > su:
        print(len(ad))
        print(*ad)
    else:
        print(0)
    return 0


main()
