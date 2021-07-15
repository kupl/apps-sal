s = input()[:-1]
while True:
    n = len(s)
    if n%2 == 0:
        if s[:n//2] == s[n//2:]:
            print(n)
            return
    s = s[:-1]

