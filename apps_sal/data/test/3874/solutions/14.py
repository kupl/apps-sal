n, m = map(int, input().split())
files = []
for _ in range(n):
    files.append(input())
toDelete = list(map(lambda s: int(s) - 1, input().split()))
pattern = files[toDelete[0]]
L = len(pattern)
for i in toDelete:
    if len(files[i]) != L:
        print('No')
        return
    for j in range(L):
        if pattern[j] != '?' and pattern[j] != files[i][j]:
            pattern = pattern[:j] + '?' + pattern[j + 1:]
for i in range(n):
    file = files[i]
    if i in toDelete or len(file) != L:
        continue
    match = True
    for j in range(L):
        if pattern[j] != '?' and pattern[j] != file[j]:
            match = False
            break
    if match:
        print('No')
        return
print('Yes')
print(pattern)
