n = int(input())
a = sorted(map(int, input().split()))
b = [0] * n
b[1::2], b[::2] = a[:n // 2], a[n // 2:]
print(sum(b[i - 1] > b[i] < b[i + 1] for i in range(1, n - 1)))
print(*b)
