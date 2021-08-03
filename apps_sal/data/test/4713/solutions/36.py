n = int(input())
s = list(input())
cnt = 0

for i in range(n):
    cnt = max(cnt, s[0:i + 1].count("I") - s[0:i + 1].count("D"))

print(cnt)
