import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    ans1 = 0
    ans2 = 0
    i = 0
    while(i < n):
        c = 1
        while (s[i] == s[i - 1]):
            c = c + 1
            i = i + 1

        if (s[i - 1] == '1'):
            ans2 = ans2 + c - 1
        else:
            ans1 = ans1 + c - 1
        i = i + 1
    print(max(ans1, ans2))
