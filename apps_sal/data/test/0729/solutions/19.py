n = int(input())
s = input()

found = False
res = ""

for i in range(n - 1):
    if s[i] != s[i + 1]:
        found = True
        res = s[i] + s[i + 1]
        break

if found:
    print("YES")
    print(res)
else:
    print("NO")
