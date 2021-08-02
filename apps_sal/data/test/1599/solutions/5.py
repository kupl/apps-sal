def main():
    s = input()
    n = int(input())

    res = [0]
    for i in range(1, len(s)):
        res.append(res[i - 1] + (s[i] == s[i - 1]))

    for _ in range(n):
        l, r = map(int, input().split())
        print(res[r - 1] - res[l - 1])


main()
