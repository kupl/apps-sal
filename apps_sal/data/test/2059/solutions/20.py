import sys

n = int(sys.stdin.readline().strip())
a = [int(item) for item in sys.stdin.readline().strip().split()]

# h_min = heapify([i for i in range(n)])
# h_max = heapify([-i for i in range(n)])
k = float('inf')
for i in range(n):
    # idx1 = heappop(h_min)
    # idx2 = heappop(h_min)
    if (i != n - 1):
        k = min(k, int(a[i] / (n - 1 - i)))
    if i:
        k = min(k, int(a[i] / i))
    # k = min(k, int(a[i] / (n - 1 - i)), int(a[i] / i))

print(k)
