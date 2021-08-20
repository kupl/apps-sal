q = int(input())
for testcase in range(q):
    n = int(input())
    s = input()
    if n == 2 and s[1] <= s[0]:
        print('NO')
    else:
        print('YES')
        print(2)
        print(s[0], s[1:])
