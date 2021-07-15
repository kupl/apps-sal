for q in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = list(map(int, input().split()))
    ans = -1
    for q in range(len(a)):
        if a[q] != s[q] and ans == -1:
            ans = s[q]-a[q]
            if ans < 0:
                print('NO')
                break
        elif a[q] != s[q] and (ans == -2 or ans != s[q] - a[q]):
            print('NO')
            break
        elif a[q] == s[q] and ans > 0:
            ans = -2
    else:
        print('YES')

