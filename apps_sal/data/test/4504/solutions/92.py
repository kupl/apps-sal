def f():
    s = list(input())
    for i in range(len(s)):
        s.pop(-1)
        s.pop(-1)
        c = 0
        for j in range(len(s) // 2):
            if s[j] == s[len(s) // 2 + j]:
                c += 1
                if c == len(s) // 2:
                    return len(s)
            else:
                break


print(f())
