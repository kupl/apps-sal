def main():
    n, k = list(map(int, input().split()))
    cnt = [0] * k
    ans = 0
    arr = list(map(int, input().split()))
    for el in arr:
        t = el % k
        if (cnt[(k - t) % k] > 0):
            cnt[(k - t) % k] -= 1
            ans += 2
        else:
            cnt[t] += 1
    print(ans)


main()
