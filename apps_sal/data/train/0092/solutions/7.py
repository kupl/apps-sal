for i in range(int(input())):
    s1 = set(input())
    s2 = set(input())
    if len(s1 & s2) > 0:
        print("YES")
    else:
        print("NO")
