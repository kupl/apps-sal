s = input()

f = False

for i in range(1, len(s)):
    if f:
        break
    for j in range(0, len(s) - i + 1):
        t = s[0:j] + s[j + i:]
        if t == "CODEFORCES":
            print("YES")
            f = True
            break

if not f:
    print("NO")
