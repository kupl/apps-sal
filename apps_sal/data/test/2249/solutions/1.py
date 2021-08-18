def main():
    n = int(input())
    a = list(map(int, input().split()))
    uniques = [0] * (n - 1) + [1]
    bools = [True] * 100001
    bools2 = [True] * 100001
    bools[a[-1]] = False
    for i in range(n - 2, 0, -1):
        temp = 0
        if bools[a[i]]:
            bools[a[i]] = False
            temp = 1
        uniques[i] = uniques[i + 1] + temp
    ret = 0
    for i in range(n - 1):
        if bools2[a[i]]:
            bools2[a[i]] = False
            ret += uniques[i + 1]
    print(ret)
    return 0


main()
