(num, limit) = list(map(int, input().split()))
l = []
for i in range(num):
    li = list(map(int, input().split()))
    if limit > min(li[1:]):
        l.append(i + 1)
print(len(l))
print(' '.join(map(str, l)))
