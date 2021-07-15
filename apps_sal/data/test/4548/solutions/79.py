N, M, X = map(int, input().split())
A = list(map(int, input().split()))
l1 = []
l2 = []

for i in A:
    if X > i:
        l1.append(i)
    else:
        l2.append(i)

print(min(len(l1), len(l2)))
