n, m = [int(i) for i in input().split(' ')]
ai = [int(i) for i in input().split(' ')]
li = []
for i in range(m):
    li.append(int(input()))

s = {ai[n - 1]}
lst = [1] * n
for i in range(n - 2, -1, -1):
    s.add(ai[i])
    lst[i] = len(s)

res = [str(lst[i - 1]) for i in li]
print('\n'.join(res))
