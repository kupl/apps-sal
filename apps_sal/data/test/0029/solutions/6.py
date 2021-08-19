s = input()
a = [0, 0, 0, 0, 0, 0]
t = []
ans = 3
for i in s:
    t.append(ord(i) - ord('0'))
for a[0] in range(10):
    for a[1] in range(10):
        for a[2] in range(10):
            for a[3] in range(10):
                for a[4] in range(10):
                    for a[5] in range(10):
                        anss = 6
                        if a[0] + a[1] + a[2] == a[3] + a[4] + a[5]:
                            for i in range(6):
                                if a[i] == t[i]:
                                    anss = anss - 1
                        if anss < ans:
                            ans = anss
print(ans)
