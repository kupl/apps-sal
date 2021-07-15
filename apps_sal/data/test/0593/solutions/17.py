n,m = list(map(int, input().split()))
candidates= n * [0]
for i in range(0, m):
    l = list(map(int, input().split()))
    candidates[l.index(max(l))] += 1


print (candidates.index(max(candidates)) + 1)
