col = int(input())
for i in range(col):
    line = input()
    if i == 0:
        a = line[0]
        b = line[1]
        if a == b:
            print('NO')
            break
    st = 0
    ed = col - 1
    while st <= ed:
        if st == i or ed == i:
            ch = a
        else:
            ch = b
        if line[st] != ch or line[ed] != ch:
            break
        st += 1
        ed -= 1
    if st <= ed:
        print('NO')
        break
else:
    print('YES')
