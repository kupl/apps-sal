tc = int(input())


def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        (n, r) = divmod(n, 3)
        nums.append(str(r))
    return list(reversed(nums))


while tc > 0:
    tc -= 1
    n = int(input())
    rep = ['0'] + ternary(n)
    idx = -1
    for i in range(len(rep)):
        if rep[i] == '2':
            idx = i - 1
            while rep[idx] != '0':
                idx -= 1
            rep[idx] = '1'
            for j in range(idx + 1, len(rep)):
                rep[j] = '0'
    ans = 0
    for j in rep:
        x = ord(j) - ord('0')
        ans = ans * 3 + x
    print(ans)
