n, _, small, big = list(map(int, input().split()))
m = list(map(int, input().split()))

diff = n - _

rd = 0

if (max(m) != big):
    rd += 1
if (min(m) != small):
    rd += 1

if min(m) < small or max(m) > big:
    print('Incorrect')
    return

#print('diff', diff)
#print('rd', rd)
#n - vsego
# m zapisal pomosh

if rd <= diff:
    print('Correct')
else:
    print('Incorrect')
