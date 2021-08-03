for _ in range(int(input())):
    n = int(input())
    count = [0] * 26
    for i in range(n):
        s = input()
        for j in s:
            count[ord(j) - 97] += 1
    temp = 0
    for i in count:
        if i % n != 0:
            temp = 1
            break
    if temp == 1:
        print('NO')
    else:
        print('YES')
