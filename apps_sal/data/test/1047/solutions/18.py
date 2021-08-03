s = list(map(int, list(input().strip())))
print(max(s))
while s:
    if s[0] == 0:
        s = s[1:]
        continue
    for i in range(len(s)):
        if s[i] != 0:
            print(1, end='')
            s[i] -= 1
        else:
            print(0, end='')
    print(end=' ')
