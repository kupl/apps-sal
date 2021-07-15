n, k, m = map(int, input().split())
a = map(int, input().split())
result, foundSolution = [[] for _ in range(m)], False
for i in a:
    result[i % m].append(i)
    if len(result[i % m]) == k:
        print('Yes')
        print(*result[i % m], sep=' ')
        foundSolution = True
        break
if not foundSolution:
    print('No')

