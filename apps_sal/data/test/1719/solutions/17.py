def ch2int(ch):
    if ch == 'A':
        return 0
    elif ch == 'C':
        return 1
    elif ch == 'G':
        return 2
    else:
        return 3


def acgt2int(agct):
    ret = 0
    for ch in agct:
        ret = (ret << 2) + ch2int(ch)
    return ret


def int2acgt(val):
    ret = []
    tmp = val
    for i in range(3):
        amari = tmp % 4
        if amari == 0:
            ret.append('A')
        elif amari == 1:
            ret.append('C')
        elif amari == 2:
            ret.append('G')
        else:
            ret.append('T')
        tmp //= 4
    ret.reverse()
    return ret


n = int(input())
dp = [[0] * 64 for _ in range(n)]

dp[0][acgt2int('TTA')] = 1
dp[0][acgt2int('TTC')] = 1
dp[0][acgt2int('TTG')] = 1
dp[0][acgt2int('TTT')] = 1


def is_valid(chs):
    tmp = ''.join(chs)
    ng = ['AGC', 'GAC', 'ACG', 'AAGC', 'ACGC', 'AGGC',
          'ATGC', 'AGAC', 'AGCT', 'AGGC', 'AGTC']
    for item in ng:
        if item in tmp:
            return False
    return True


for i in range(1, n):
    for j in range(64):
        chs = int2acgt(j)
        tmp = 0
        for ch in ['A', 'C', 'G', 'T']:
            my_chs1 = [ch] + chs
            if is_valid(my_chs1):
                tmp += dp[i-1][acgt2int(my_chs1[:-1])] % (10 ** 9 + 7)
        dp[i][j] = tmp

print((sum(dp[-1]) % (10 ** 9 + 7)))

