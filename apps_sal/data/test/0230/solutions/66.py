n = int(input())
s = input()
MOD = 10 ** 18 + 7
A = 123456


def ok(l):
    rolling_hash = 0
    strings = {}
    for i in range(n):
        rolling_hash *= A
        rolling_hash += ord(s[i])
        if i - l >= 0:
            rolling_hash -= ord(s[i - l]) * pow(A, l, MOD)
        rolling_hash %= MOD
        if i < l - 1:
            continue
        if rolling_hash not in strings:
            strings[rolling_hash] = []
        strings[rolling_hash].append(i)
    for string in strings:
        if strings[string][-1] - strings[string][0] >= l:
            return True
    return False


(bottom, top) = (0, n)
while top - bottom > 1:
    mid = (top + bottom) // 2
    if ok(mid):
        bottom = mid
    else:
        top = mid
print(bottom)
