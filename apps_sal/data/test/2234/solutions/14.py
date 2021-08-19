t = int(input())
for it in range(t):
    (n, k) = [int(i) for i in input().split()]
    if n >= k:
        print(0 if n % 2 == k % 2 else 1)
    else:
        print(k - n)
