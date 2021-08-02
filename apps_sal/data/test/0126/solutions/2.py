n = int(input())
d = list(map(int, input()))

l = all([i not in d for i in [1, 4, 7, 0]])
r = all([i not in d for i in [3, 6, 9, 0]])
u = all([i not in d for i in [1, 2, 3]])
d = all([i not in d for i in [7, 0, 9]])
print('NO' if l or r or u or d else 'YES')
