for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()

    d = []
    for i in range(n):
        if s[i] != t[i]:
            d.append(i)

    if len(d) != 2:
        print("No")
    else:
        i, j = d
        if s[i] == s[j] and t[i] == t[j]:
            print("Yes")
        else:
            print("No")
