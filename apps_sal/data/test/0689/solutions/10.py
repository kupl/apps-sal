for _ in range(int(input())):
    n = int(input())
    u = []
    for i in range(n):
        u += list(input())
    abc = [0] * 26
    for i in range(len(u)):
        abc[ord(u[i]) - ord('a')] += 1
    for i in range(26):
        if abc[i] % n != 0:
            print('NO')
            break
    else:
        print('YES')
        

