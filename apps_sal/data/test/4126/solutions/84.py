s = input()
if s[:] == s[::-1]:
    a = s[:((len(s) - 1) // 2)]
    if a[:] == a[::-1]:
        b = s[((len(s) + 2) // 2):]
        if b[:] == b[::-1]:
            print("Yes")
            return
print("No")
