input()
L = list(map(int, input().split()))
print(('No', 'Yes')[sum(L) > max(L) * 2])
