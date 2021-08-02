t = int(input())
for j in range(t):
    s = input()
    l = len(s)
    ans = 0
    A = []
    i = 0
    while i < l - 2:
        if s[i:i + 3] == "one":
            ans += 1
            A.append(i + 2)
            i += 3
        elif s[i:i + 3] == "two":
            ans += 1
            if i + 5 <= l and s[i + 2:i + 5] == "one":
                A.append(i + 3)
                i += 5
            else:
                A.append(i + 2)
                i += 3
        else:
            i += 1
    print(ans)
    print(" ".join(list(map(str, A))))
