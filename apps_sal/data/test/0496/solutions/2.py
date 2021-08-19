s = input().split()
for i in range(4):
    s[i] = int(s[i])
if s[1] - s[0] == s[2] - s[1] == s[3] - s[2]:
    d = s[1] - s[0]
    if (s[3] + d) % 1 == 0:
        print(s[3] + d)
    else:
        print(42)
elif s[1] / s[0] == s[2] / s[1] == s[3] / s[2]:
    d = s[1] / s[0]
    if int(s[3] * d) != s[3] * d:
        print(42)
    else:
        print(int(s[3] * d))
else:
    print(42)
