N = input()
L = sorted(list(map(int, input().split())))
print('No' if max(L) >= sum(L[:-1]) else 'Yes')
