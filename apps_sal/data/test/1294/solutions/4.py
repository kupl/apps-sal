for i in range(int(input())):
    s = input()
    working = []
    j = 0
    while j < len(s):
        nextJ = j+1
        while nextJ < len(s) and s[nextJ] == s[j]:
            nextJ += 1
        if (nextJ - j) % 2 == 1:
            if s[j] not in working:
                working.append(s[j])
        j = nextJ
    working.sort()
    print("".join(working))

