for _ in range(int(input())):
    a, b, p = list(map(int, input().split()))
    s = input()
    naw = 0
    for q in range(len(s) - 2, -1, -1):
        if (q == len(s) - 2 or s[q] != s[q + 1]) and naw + (a if s[q] == 'A' else b) > p:
            print(q + 2)
            break
        elif q == len(s) - 2 or s[q] != s[q + 1]:
            naw += (a if s[q] == 'A' else b)
    else:
        print(1)
