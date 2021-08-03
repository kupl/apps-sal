n, k = [int(i) for i in input().split()]
data = [int(i) for i in input().split()]
span = data[-1] - data[0]
delta = [data[i + 1] - data[i] for i in range(n - 1)]
delta.sort(reverse=True)
print(span - sum(delta[:k - 1]))
