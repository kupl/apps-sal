# arc109c
def win(i, j):
    if i == j:
        return i
    if i == 'R' and j == 'P':
        return 'P'
    if i == 'P' and j == 'R':
        return 'P'

    if i == 'P' and j == 'S':
        return 'S'
    if i == 'S' and j == 'P':
        return 'S'

    if i == 'S' and j == 'R':
        return 'R'
    if i == 'R' and j == 'S':
        return 'R'


def step(S, k):
    T = S + S
    tmp = ''
    for i in range(len(S)):
        tmp += win(T[2*i], T[2*i+1])
    return tmp, k-1


n, k = list(map(int, input().split()))
s = input()
now = s
rem = k

while rem > 0:
    now, rem = step(now, rem)

print((now[0]))

