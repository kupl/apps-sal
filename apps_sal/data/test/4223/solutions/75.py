n = int(input())
s = input()
a = ''
cnt = 0
for i in range(n):
    if i == 0:
        a += s[i]
        cnt += 1
    elif s[i] != a[-1]:
        a += s[i]
        cnt += 1
print(cnt)
