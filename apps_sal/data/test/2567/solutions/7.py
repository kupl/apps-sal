for _ in range (int(input())):
    n = int(input())
    s=input()
    char = s[n-1]
    ans = ''
    for i in range (n):
        ans += char
    print(ans)
