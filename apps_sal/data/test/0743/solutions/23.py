def log(*args):
    pass


N = int(input())
L = [int(n) for n in input().split()]
assert N == len(L)
L.sort()
changed = True
while changed:
    log('begin, L=', L)
    blah = L[:]
    changed = False
    for i in range(N):
        for j in range(i):
            num = L[i] + L[j]
            if num not in blah:
                blah.append(num)
    log('blah', blah)
    for i in range(N):
        num = L[i]
        for n in range(num - 1, -1, -1):
            if n in blah:
                log('pos', i, 'subtracting', n, 'from', L[i])
                L[i] = num - n
                changed = True
                break
    log(sum(L))
log('fin')
print(sum(L))
