s = input()
for i in range(len(s) - 1, -1, -1):
    if i % 2 == 0 and s[:i // 2] == s[i // 2:i]:
        print(i)
        break
