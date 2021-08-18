s = input()
n = int(input())
one = len(s) // n
if len(s) % n != 0:
    print('NO')
    return
for i in range(0, len(s), one):
    our = s[i:i + one]
    if our != our[::-1]:
        print('NO')
        return
print('YES')
