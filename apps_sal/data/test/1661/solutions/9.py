def main():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ind = 0
    g = 0
    ret = 0
    while ind < m and g < n:
        if c[g] <= a[ind]:
            ret += 1
            ind += 1
        g += 1
    print(ret)
    return 0


main()
