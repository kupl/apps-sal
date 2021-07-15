def resolve():
    n = int(input())
    s = input()
    ans = s[0]
    for i in range(1,n):
        if s[i] != ans[-1]:
            ans += s[i]
    print(len(ans))
resolve()
