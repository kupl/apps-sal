t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    if n == k:
        print(0)
        continue
    if k < n and k % 2 != n % 2:
        print(1)
        continue
    if k < n:
        print(0)
        continue
    print(k - n)
