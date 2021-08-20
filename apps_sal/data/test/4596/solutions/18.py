def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    ans = 0
    while True:
        for i in range(n):
            if a[i] % 2 != 0:
                return ans
            a[i] = a[i] // 2
        ans += 1


print(main())
