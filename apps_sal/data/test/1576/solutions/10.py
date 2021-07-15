s = input()
if len(s) % 2 == 0:
    st = ''
    for i in range(len(s) // 2):
        st += s[len(s) - 1 - i] + s[i]
    print(st[::-1])
else:
    st = ''
    for i in range(len(s) // 2):
        st += s[i] + s[len(s) - 1 - i]
    st += s[len(s) // 2]
    print(st[::-1])

