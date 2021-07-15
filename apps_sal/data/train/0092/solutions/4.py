q = int(input())
for i in range(q):
    a = input()
    b = input()
    done = False
    for i in a:
        if i in b:
            done = True
            break
    print('YES' if done else 'NO')
