(N, K) = input().split()
A = dict()
for i in input().split():
    if int(i) in A:
        A[int(i)] += 1
    else:
        A[int(i)] = 1
hoge = []
for i in A.values():
    hoge.append(i)
hoge.sort()
sum = 0
changed = 0
while len(hoge) - changed > int(K):
    sum += hoge[changed]
    changed += 1
print(sum)
