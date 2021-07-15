s = input()
max = len(s) - 1
for i in range(len(s) - 1, -1, -1):
    if int(s[i]) % 2 == 0 and (s[-1] > s[i] or max == len(s) - 1):
        max = i
if max == len(s) - 1:
    print(-1)
else:
    print(s[:max] + s[-1] + s[max + 1 : -1] + s[max])

