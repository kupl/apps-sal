s = list(input())

s = s[:len(s) - 1]

for i in range(len(s)):
    if len(s) % 2 == 0:
        if s[:len(s) // 2] == s[len(s) // 2:]:
            print(len(s))
            return
    s.pop(-1)
