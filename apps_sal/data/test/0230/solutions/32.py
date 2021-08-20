n = int(input())
s = input()
A = 1234567
MOD = 10000000000000007


def ok(length):
    rolling_hash = 0
    head = pow(A, length, MOD)
    occurence = {}
    for i in range(n):
        rolling_hash = (rolling_hash * A + ord(s[i])) % MOD
        if i - length >= 0:
            rolling_hash = (rolling_hash - head * ord(s[i - length])) % MOD
        if rolling_hash not in occurence:
            occurence[rolling_hash] = []
        occurence[rolling_hash].append(i)
    for key in occurence:
        if occurence[key][-1] - occurence[key][0] >= length:
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
