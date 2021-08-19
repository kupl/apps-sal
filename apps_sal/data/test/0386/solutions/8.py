_ = int(input())

mini = - 10**9 - 1
maxi = 10**9 + 1

for i in range(_):
    s, n, a = input().split()
    n = int(n)
#    print('\n---')
#    print(s, n, a)
#    print('----')
    if a == 'Y':
        if s == '>=':
            mini = max(mini, n)
        elif s == '>':
            mini = max(mini, n + 1)
        elif s == '<=':
            maxi = min(maxi, n)
        elif s == '<':
            maxi = min(maxi, n - 1)
    else:
        if s == '>=':
            maxi = min(maxi, n - 1)
        elif s == '>':
            maxi = min(maxi, n)
        elif s == '<=':
            mini = max(mini, n + 1)
        elif s == '<':
            mini = max(mini, n)

#    print(mini, maxi, '\n--------')

if maxi >= mini:
    print(mini)
else:
    print('Impossible')
