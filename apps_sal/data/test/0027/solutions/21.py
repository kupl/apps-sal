n = input()
s = input()
best = 0
for i in range(len(s) // 2 + 1):
    t = s[:i] * 2
    # print(t)
    try:
        if s.index(t) == 0:
            best = i
    except:
        pass
if best > 0:
    print(len(s) - best + 1)
else:
    print(len(s))
