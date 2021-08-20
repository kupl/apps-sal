def main():
    n = int(input())
    s = input()
    (a, b, ans) = (0, 0, 0)
    cnt = 1
    for i in range(n):
        if s[i] == '?':
            ans = (ans * 3 + b) % 1000000007
            b = (b * 3 + a) % 1000000007
            a = (a * 3 + cnt) % 1000000007
            cnt = cnt * 3 % 1000000007
        elif s[i] == 'c':
            ans = (ans + b) % 1000000007
        elif s[i] == 'b':
            b = (b + a) % 1000000007
        elif s[i] == 'a':
            a = (a + cnt) % 1000000007
    print(ans)


tn = 1
for _ in range(tn):
    main()
