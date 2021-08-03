def palindrom(s):
    n = len(s)
    for num in range(n):
        if s[num] != s[n - num - 1]:
            return 0
    return 1


s = input()
n = len(s)
words = "abcdefghjklmnpoqrstvwxyziuy"
yes = 0
s1 = ""
for i in range(n + 1):
    for j in words:
        if palindrom(s[:i] + j + s[i:]) == 1:
            s1 = s[:i] + j + s[i:]
            yes = 1
            break
    if yes == 1:
        break
if s1 == "":
    print("NA")
else:
    print(s1)
