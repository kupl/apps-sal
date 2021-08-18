s = input()
n = len(s)

if s == s[::-1]:
    check = s[0:(n - 1) // 2]
    if check == check[::-1]:
        check = s[(n + 3) // 2 - 1:]
        if check == check[::-1]:
            print("Yes")
            return
print("No")
