n = int(input())
i = n
while True:
    s = str(i)
    su = 0
    for j in range(len(s)):
        su += int(s[j])
    if su % 4 == 0:
        print(i)
        break
    i += 1
