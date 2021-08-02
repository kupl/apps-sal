n = int(input())
s = input()
i = 0
d = ""
ls = []
mx = -1
while i < n:
    temp = s[0:i + 1]
    for j in range(i + 1, n + 1):
        if temp == s[i + 1:j]:
            mx = max(mx, len(temp))
    i += 1
if mx > 0:
    print(len(temp) - mx + 1)
else:
    print(len(temp))
