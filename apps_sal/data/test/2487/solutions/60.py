n = int(input())
vertex = [(1 + n - i) * (n - i) // 2 for i in range(n)]
side = [0] * (n - 1)
for i in range(n - 1):
    (l, r) = list(map(int, input().split()))
    if l > r:
        (l, r) = (r, l)
    side[i] = l * (n - r + 1)
print(sum(vertex) - sum(side))
