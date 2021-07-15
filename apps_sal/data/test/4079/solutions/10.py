n = int(input())

for i in range(n):
    s = input()
    s1 = ''.join(sorted(s))
    z = set()
    fl = 0

    for j in range(len(s1) - 1):
        if abs(ord(s1[j]) - ord(s1[j + 1])) != 1:
            print('No')
            fl = 1
            break

    if fl == 0:
        print('Yes')
