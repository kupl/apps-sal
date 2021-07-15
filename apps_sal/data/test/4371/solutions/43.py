s = input()
res = 1000
for i in range(len(s) - 2):
    res = min(res, abs(753 - int(s[i : i + 3])))
print(res)

