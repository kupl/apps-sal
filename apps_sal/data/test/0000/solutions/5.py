s = input()
t_d = 0
try:
    left = -1
    was_b = False
    for i in range(len(s)):
        if s[i] == '[' and not was_b:
            was_b = True
            continue
        if s[i] == ':' and was_b:
            left = i
            break
        t_d += 1
    if left == -1:
        raise ArithmeticError()
    right = -1
    was_b = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ']' and not was_b:
            was_b = True
            continue
        if s[i] == ':' and was_b:
            right = i
            break
        t_d += 1
    if right == -1 or right <= left:
        raise ArithmeticError()
    for i in range(left + 1, right):
        if s[i] != '|':
            t_d += 1
    print(len(s) - t_d)
except:
    print(-1)
        

