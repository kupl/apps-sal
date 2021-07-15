s = input()
size = len(s) // 2 + 1
for i in range(size, len(s)):
    if s[:i] == s[-i:]:
        print("YES")
        print(s[:i])
        break
else:
    print("NO")
