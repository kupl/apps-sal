def main():
    arr = [0] * 26
    for i in range(int(input())):
        s = input()
        s = ord(s[0]) - ord('a')
        arr[s] += 1
    ans = 0
    for i in range(26):
        a = arr[i] // 2
        b = arr[i] - a
        ans += a * (a - 1)
        ans += b * (b - 1)
    print(ans >> 1)
    return 0


main()
