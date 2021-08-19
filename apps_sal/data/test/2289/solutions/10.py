import bisect


def find_ge(a, key):
    '''Find smallest item greater-than or equal to key.
    Raise ValueError if no such item exists.
    If multiple keys are equal, return the leftmost.
    '''
    i = bisect.bisect_left(a, key)
    if i == len(a):
        return -1
    return i


n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
k = [int(x) for x in input().split()]
result = [0] * (q + 1)
result[0] = n
s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]

remain = 0
attack = 0
for i in range(1, q + 1):
    attack += k[i - 1]

    ge = find_ge(s, attack)

    if ge >= 0:
        remain = s[ge] - attack
        #print(remain, s[ge], i)
        if remain > 0:
            result[i] = n - ge
        else:
            result[i] = n - ge - 1
        if result[i] == 0:
            result[i] = n
            attack = 0
    else:
        result[i] = n
        attack = 0
        remain = 0
    '''
    else:
        # all soldiers died
        remain -= k[i-1]
        attack = 0
        if remain > 0: result[i] = n-ge
        else: result[i] = n-ge-1
    '''

print('\n'.join(str(x) for x in result[1:]))
