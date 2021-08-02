for case in range(int(input())):
    n = int(input())
    s = input()
    ans = 'NO'
    for i in range(n - 10):
        if s[i] == '8':
            ans = 'YES'
            break
    print(ans)
