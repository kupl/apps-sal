n = int(input())
s = input()
t = input()

ab = []
ba = []

for i in range(n):
    if s[i] == t[i]:
        continue
    else:
        if s[i] == "a":
            ab.append(i)
        else:
            ba.append(i)

if (len(ab) + len(ba)) % 2 == 0:
    ans = []
    for i in range(len(ab) // 2):
        ans.append([ab[2 * i], ab[2 * i + 1]])
    for i in range(len(ba) // 2):
        ans.append([ba[2 * i], ba[2 * i + 1]])
    if len(ab) % 2 != 0:
        ans.append([ab[-1], ab[-1]])
        ans.append([ab[-1], ba[-1]])
    print(len(ans))
    for i, j in ans:
        print(i + 1, j + 1)

else:
    print(-1)
