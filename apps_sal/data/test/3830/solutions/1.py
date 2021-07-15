def main():
    n = int(input())
    # arr = list(map(int, input().split()))
    # x1, y1, x2, y2 = map(int, input().split())
    s = input()
    if '>' not in s:
        print(n)
    elif '<' not in s:
        print(n)
    else:
        ans = 0
        for i in range(n):
            l = (i - 1 + n) % n
            # r = (i + 1) % n
            if s[i] == '-' or s[l] == '-':
                ans += 1
        print(ans)


# for _ in range(1):
for _ in range(int(input())):
    main()

