a, b = map(int, input().split())
s = input()
for i in s[0:a]:
    if 48 <= ord(i) and ord(i) <= 57:
        continue
    else:
        print("No")
        return
if s[a] != "-":
    print("No")
    return
for i in s[a + 1:a + b + 1]:
    if 48 <= ord(i) and ord(i) <= 57:
        continue
    else:
        print("No")
        return
print("Yes")
