for _ in range(int(input())):
    n = int(input())
    s = input()
    ans1 = 0
    ans2 = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            if s[i] == '0':
                ans1 += 1
            else:
                ans2 += 1
    print(max(ans1, ans2))
