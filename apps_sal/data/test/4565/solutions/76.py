n = int(input())
s = input()
wcnt = [0] * n
ecnt = [0] * (n)
enum = 0
wnum = 0
for i in range(n):
    if s[i] == "W":
        wnum += 1
    wcnt[i] += wnum
    if s[-i - 1] == "E":
        enum += 1
    ecnt[-i - 1] += enum
ans = 10 ** 10
for i in range(n):
    temp = 0
    if i - 1 >= 0:
        temp += wcnt[i - 1]
    if i + 1 < n:
        temp += ecnt[i + 1]
    ans = min(ans, temp)
print(ans)
