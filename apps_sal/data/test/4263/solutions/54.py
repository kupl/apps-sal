s = input()
cnt = 0
max = 0
for i in range(0, len(s)):
    if s[i] in ["A", "C", "G", "T"]:
        cnt += 1
    else:
        if max < cnt:
            max = cnt
        cnt = 0
if max < cnt:
    max = cnt
cnt = 0
print(max)
