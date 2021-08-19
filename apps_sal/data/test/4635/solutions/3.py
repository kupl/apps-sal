alph = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    s = alph[:k]
    print(s * (n // k) + alph[:n % k])
