(n, k) = map(int, input().split())
(n, c) = (set(range(1, n + 1)), set())
for i in range(k):
    input()
    c |= set(map(int, input().split()))
print(len(n ^ c))
