n = int(input())

s = []
for i in range(n):
    s.append(input())

s.sort(key=len)

yes = True
for i in range(n - 1):
    if s[i] not in s[i + 1]:
        yes = False
        break

if yes:
    print("YES")
    print("\n".join(s))
else:
    print("NO")
