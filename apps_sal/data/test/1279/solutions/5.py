def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in range(n):
        if a[i] & 1:
            odd += 1
        else:
            even += 1
    b = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        if b[i] & 1:
            if even:
                even -= 1
                ans += 1
        else:
            if odd:
                odd -= 1
                ans += 1
    print(ans)
    return 0

main()
