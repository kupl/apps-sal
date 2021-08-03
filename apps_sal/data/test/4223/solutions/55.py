n = int(input())
s = list(input())
color = s[0]
cnt = 1
for i in range(1, n):
    if s[i] != color:
        color = s[i]
        cnt += 1
print(cnt)
