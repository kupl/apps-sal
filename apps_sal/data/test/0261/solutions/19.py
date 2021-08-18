n = input()
s = input()

good = False

for i in range(0, int(n)):
    for j in range(1, 27):
        try:
            if s[i] == '*' and s[i + j] == '*' and s[i + 2 * j] == '*' and s[i + 3 * j] == '*' and s[i + 4 * j] == '*':
                good = True
        except:
            pass

if good:
    print("yes")
else:
    print("no")
