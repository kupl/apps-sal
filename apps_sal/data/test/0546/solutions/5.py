import string


def single_check(p, a):
    if not p:
        return 1
    if len(a) != len(p):
        return 0
    else:
        for i in range(len(a)):
            if p[i] != a[i] and p[i] != '?' or (p[i] == '?' and a[i] not in good):
                break
        else:
            return 1
        return 0


good = input()
bad = set(string.ascii_lowercase) - set(good)
pattern = input()
n = int(input())
patspl = pattern.split('*')
for _ in range(n):
    a = input()
    if len(patspl) == 1:
        print('YES' if single_check(pattern, a) else 'NO')
    elif len(a) < len(pattern) - 1:
        print('NO')
    elif single_check(patspl[0], a[:len(patspl[0])]) and single_check(patspl[1], a[-len(patspl[1]):]):
        for c in a[len(patspl[0]):-len(patspl[1]) or len(a)]:
            if c not in bad:
                print('NO')
                break
        else:
            print('YES')
    else:
        print('NO')
