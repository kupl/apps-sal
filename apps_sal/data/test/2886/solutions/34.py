s = input()
size = len(s)
if size == 2:
    if s[0] == s[1]:
        print("1 2")
    else:
        print("-1 -1")
else:
    for i in range(2, size):
        a = s[i]
        b = s[i - 1]
        c = s[i - 2]
        if a == b or b == c or a == c:
            print(i - 1, i + 1)
            break
    else:
        print("-1 -1")
