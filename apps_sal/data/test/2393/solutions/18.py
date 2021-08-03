t = int(input())
for _ in range(t):
    s = input()
    a = []
    n = len(s)
    if s.count("two") + s.count("one") == 0:
        ans = 0
    else:
        ans = 0
        for i in range(n):
            if i + 4 < n:
                if s[i:i + 5] == "twone":
                    ans += 1
                    a.append(str(i + 3))
                elif i + 2 < n:
                    if s[i:i + 3] == "one" and s[i - 2:i + 3] != "twone" or s[i:i + 3] == "two":
                        ans += 1
                        a.append(str(i + 2))
            elif i + 2 < n:
                if s[i:i + 3] == "one" and s[i - 2:i + 3] != "twone" or s[i:i + 3] == "two":
                    ans += 1
                    a.append(str(i + 2))
    print(ans)
    print(" ".join(a))
