N = int(input())
s = list(input())

cnt = 0
for i in range(len(s) - 2):
    if s[i] + s[i + 1] + s[i + 2] == "ABC":
        cnt += 1

print(cnt)
