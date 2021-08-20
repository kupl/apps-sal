def readln():
    return tuple(map(int, input().split()))


(n,) = readln()
sms = '<3'.join([''] + [input() for _ in range(n)] + [''])
s = 0
for c in list(input()):
    if sms[s] == c:
        s += 1
    if s == len(sms):
        break
print('yes' if s == len(sms) else 'no')
