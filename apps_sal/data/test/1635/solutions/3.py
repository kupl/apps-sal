def main():
    def read(): return tuple(map(int, input().split()))
    n = read()[0]
    l = read()
    last = {}
    for i in range(n):
        last[l[i]] = i
    mn = 1e10
    ans = -1
    for k in last:
        if last[k] < mn:
            ans = k
            mn = last[k]
    print(ans)


main()
