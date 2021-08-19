for i in range(int(input())):
    s = list(input())
    n = len(s)

    for i in range(n - 1):
        if s[i] == s[i + 1] and s[i] != "?":
            print(-1)
            break
    else:
        if n == 1:
            if s[0] == "?":
                s[0] = "a"
            print("".join(s))
            continue
        if s[0] == "?":
            for j in "abc":
                if s[1] != j:
                    s[0] = j
                    break

        for i in range(1, n - 1):
            if s[i] == "?":
                for j in "abc":
                    if s[i + 1] != j and s[i - 1] != j:
                        s[i] = j
                        break
            # print(s)
        if s[-1] == "?":
            for j in "abc":
                if j != s[-2]:
                    s[-1] = j
                    break
        print("".join(s))
