s = input() + "R"


p = [0] * (len(s) - 1)
key = s[0]
strt = 0
for i in range(len(s)):

    if key != s[i]:
        if key == "R":
            p[i] += (i - strt) // 2
            p[i - 1] += (i - strt) // 2 + (i - strt) % 2
            key = "L"
        else:
            p[strt] += (i - strt) // 2 + (i - strt) % 2
            p[strt - 1] += (i - strt) // 2
            key = "R"
        strt = i

for i in p:
    print(i, end=" ")
