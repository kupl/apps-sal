s = input()
t = input()
cnt = 0
for i in range(3):
    cnt += s[i] == t[i]
print(cnt)
