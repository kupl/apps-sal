from collections import Counter

N = int(input())
A = list([int(x) for x in input().split()])

result = dict(Counter(A))

for i in range(1, N+1):
    if i in result:
        print((result[i]))
    else:
        print((0))


