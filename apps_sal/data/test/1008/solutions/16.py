s = input()
b = [int(s) for s in input().split()][0]
a = list()
if len(s) % b:
    print('NO')
else:
    for i in range(0, len(s) - len(s) // b + 1, len(s) // b):
        a.append(s[i:i + len(s) // b])
    for i in a:
        if not i == i[::-1]:
            print('NO')
            break
    else:
        print('YES')
