3

def isgood(n):
    if n == '1' or n == '14' or n == '144':
        return True
    if n.startswith('144'):
        return isgood(n[3:])
    if n.startswith('14'):
        return isgood(n[2:])
    if n.startswith('1'):
        return isgood(n[1:])
    return False

n = input()
if isgood(n):
    print('YES')
else:
    print('NO')

