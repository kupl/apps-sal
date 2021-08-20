n = int(input())
for _ in range(n):
    input()
    s = input()
    for i in range(len(s) // 2):
        val = abs(ord(s[i]) - ord(s[-1 - i]))
        if val != 0 and val != 2:
            print('NO')
            break
    else:
        print('YES')
