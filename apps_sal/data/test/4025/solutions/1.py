def f(a, b, c):
    kek = [a, b, c]
    arr = [0, 0, 1, 2, 0, 2, 1] * 100
    ans = 0
    for i in range(7):
        tmp = kek + []
        j = i
        while tmp[arr[j]]:
            tmp[arr[j]] -= 1
            j += 1
        ans = max(ans, j - i)
    return ans

def main():
    a, b, c = map(int, input().split())
    d = min(a // 3, b >> 1, c >> 1)
    ans = 7 * d
    a -= 3 * d
    b -= d << 1
    c -= d << 1
    ans += f(a, b, c)
    print(ans)
    return 0

main()
