t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    n1 = n % k
    k1 = int(k / 2)
    if n1 <= k1:
        print(n)
    else:
        print(n - n1 + k1)
