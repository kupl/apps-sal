(n, k) = list(map(int, input().split(' ')))
numbers = [int(i) for i in input().split(' ')]
numbers = [(num, i + 1) for (i, num) in enumerate(numbers)]
numbers = sorted(numbers)
numbers = numbers[::-1][:k]
indices = [i[1] for i in numbers]
indices = sorted(indices)
for i in range(k - 1, 0, -1):
    indices[i] -= indices[i - 1]
s = sum(indices)
indices[-1] += n - s
print(sum([i[0] for i in numbers]))
print(*indices)
