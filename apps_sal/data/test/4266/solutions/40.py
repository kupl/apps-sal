k, x = map(int, input().split())
li = []
for i in range(x - (k - 1), x + k):
    li.append(str(i))

print(' '.join(li))
