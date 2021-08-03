s = input()
n = len(s)
for i in range(n // 2 + 1, n):
    if s[0:i] == s[n - i:n]:
        print("YES")
        print(s[0:i])
        return
print("NO")
