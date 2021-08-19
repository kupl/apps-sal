for _ in range(int(input())):
    n, k = tuple(map(int, input().split()))
    s = list(input())
    ans = list("()" * (k - 1) + "(" * ((n // 2) - k + 1) + ")" * (n // 2 - k + 1))
    ops = []
    i = 0
    while ans != s and i < n:
        # print("----" , i, "----")
        if ans[i] != s[i]:
            j = s[i:].index(ans[i]) + i
            # print(0,"|",j, s[j], s[i])
            ops.append(str(i + 1) + " " + str(j + 1))
            for k in range(i, (j + i + 1) // 2):
                # print(11, "|", j, s[k], s[j + i - k])
                (s[k], s[j + i - k]) = (s[j + i - k], s[k])
                # print(12, "|", j, s[k], s[j + i - k])
        # print(" ".join(s))
        # print(" ".join(ans))
        # print("|".join(ops))
        i += 1
    print(len(ops))
    if len(ops) != 0:
        print("\n".join(ops))
