from collections import Counter

N, K = list(map(int, input().split()))
A = Counter(list(map(int, input().split())))

if(len(A) > K):
    values, counts = list(zip(*A.most_common()[-(len(A)-K):]))
    print((sum(counts)))
else:
    print((0))

