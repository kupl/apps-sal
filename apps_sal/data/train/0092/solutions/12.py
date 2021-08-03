q = int(input())
for i in range(q):
    s1 = input()
    s2 = input()
    if len(set(s1) & set(s2)) > 0:
        print('YES')
    else:
        print('NO')
