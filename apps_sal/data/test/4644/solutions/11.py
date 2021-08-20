def solve(arr, n):
    even = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
    if even == n:
        print('NO')
        return
    odd = n - even
    if odd == n and n % 2 == 0:
        print('NO')
        return
    print('YES')


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, n)


main()
