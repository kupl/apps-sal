(n, k) = map(int, input().strip().split())
ids = map(int, input().strip().split())
convs = []
for i in ids:
    if i in convs:
        continue
    elif len(convs) == k:
        convs.pop()
    convs.insert(0, i)
print(len(convs))
print(' '.join(map(str, convs)))
