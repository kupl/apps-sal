for i in range(int(input())):
    n = int(input())
    s = input()
    if '8' in s:
        if n - s.index('8') >= 11:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
