def main():
    n = int(input())
    a = sorted(map(abs, list(map(int, input().split()))))
    i = 0
    res = 0
    for j in range(n):
        while a[i] * 2 < a[j]:
            i += 1
        res += j - i
    print(res)


main()
