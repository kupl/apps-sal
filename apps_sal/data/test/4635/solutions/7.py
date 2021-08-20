alpha = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
for test in range(t):
    (n, k) = list(map(int, input().split()))
    print(alpha[0:k] * (n // k) + alpha[:n % k])
