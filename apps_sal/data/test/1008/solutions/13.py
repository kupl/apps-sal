s = input()
n = int(input())

wordlength = len(s) // n
if wordlength * n != len(s):
    print("NO")
else:
    current = wordlength
    word = 0
    yes = True
    for i in range(n):
        if not yes:
            break
        for j in range(wordlength):

            if s[i * wordlength + j] != s[(i + 1) * wordlength - j - 1]:
                yes = False
                break

    if yes:
        print("YES")
    else:
        print("NO")
