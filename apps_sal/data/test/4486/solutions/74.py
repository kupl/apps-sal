s = input()
if len(s) % 2 == 0:
    f = len(s) // 2
else:
    f = len(s) // 2 + 1
for i in range(f):
    print(s[2 * i], end="")
