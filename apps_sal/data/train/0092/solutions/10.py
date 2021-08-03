for _ in range(int(input())):
    s, t = input(), input()
    k = "NO"
    for i in s:
        if i in t:
            k = "YES"
            break
    print(k)
