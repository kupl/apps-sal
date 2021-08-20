n = int(input())
(T, A) = map(int, input().split())
for _ in range(n - 1):
    (t, a) = map(int, input().split())
    x = max(-(-T // t), -(-A // a))
    T = x * t
    A = x * a
print(T + A)
