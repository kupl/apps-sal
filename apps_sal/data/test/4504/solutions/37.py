s = input()
for i in range(1000):
    s = s[:-2]
    tnp = 0
    for j in range(len(s) // 2):
        if s[j] != s[len(s) // 2 + j]:
            tnp += 1
    if tnp == 0:
        print(len(s))
        break
