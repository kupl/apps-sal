n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))

indexed_a = list(zip(a, list(range(n))))

sorted_indexed_a = list(reversed(sorted(indexed_a)))

sorted_a = list(reversed(sorted(a)))

partition = list(sorted([y for x,y in sorted_indexed_a[:(m*k)]]))
print(sum(sorted_a[:(m*k)]))
result = [x + 1 for x in partition[(m-1)::m]]
print(' '.join([ str(x) for x in result[:-1]]))

