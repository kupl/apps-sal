t = int(input())
al = 'abcdefghijklmnopqrstuvwxyz'
for i in range(t):
    (n, k) = list(map(int, input().split()))
    l = n // k
    s = al[:k] * l
    s += al[:n % k]
    print(s)
