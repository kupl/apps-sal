N = int(input())
(takahashi, aoki) = (1, 1)
for _ in range(N):
    (a, b) = map(int, input().split())
    c = max((takahashi - 1) // a + 1, (aoki - 1) // b + 1)
    takahashi = c * a
    aoki = c * b
print(takahashi + aoki)
