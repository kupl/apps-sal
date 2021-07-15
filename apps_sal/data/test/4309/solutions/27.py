n = int(input())
while True:
    s = str(n)
    if s[0] == s[1] and s[0] == s[2]:
        print(n)
        break
    n += 1
