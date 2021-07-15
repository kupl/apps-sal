state = 1

s = input()


if ((s.count('a') == 0) or (s.count('b') == 0) or ((s.count('c') != s.count('a') and (s.count('c') != s.count('b'))))):
    print('NO')
    return

for el in s:
    if el == 'b':
        state = max(state, 2)
    if el == 'c':
        state = max(state, 3)
    if state != 1 and el == 'a':
        print("NO")
        return
    if state != 2 and el == 'b':
        print("NO")
        return
    if state != 3 and el == 'c':
        print("NO")
        return
        
print("YES")
