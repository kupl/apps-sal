s = input()
i = len(s) - 1
while True:
    if i % 2 == 0:
        if s[: i//2] == s[i//2 : i]:
            print(i)
            break
    i -= 1
