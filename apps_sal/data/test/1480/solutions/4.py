(n, k) = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split()))
children = list([i + 1 for i in range(n)])
answer = []
i = 0
for ai in arr:
    i = (i + ai) % n
    answer.append(str(children[i]))
    del children[i]
    n -= 1
print(' '.join(answer))
