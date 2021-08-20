def main():
    n = int(input())
    s = input()
    g = 'ACTG'
    mi = 1000000000
    for i in range(n - 3):
        a = s[i:i + 4]
        arr = [ord(g[i]) - ord(a[i]) for i in range(4)]
        kek = [ord(a[i]) - ord(g[i]) for i in range(4)]
        ans = 0
        for i in range(4):
            if arr[i] < 0:
                arr[i] += 26
            if kek[i] < 0:
                kek[i] += 26
            ans += min(arr[i], kek[i])
        mi = min(mi, ans)
    print(mi)
    return 0


main()
