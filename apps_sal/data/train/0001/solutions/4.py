q = int(input())
for i in range(q):
    (a, b, k) = list(map(int, input().split()))
    if a < b:
        (a, b) = (b, a)
    if a > k:
        print(-1)
    elif a % 2 == b % 2 != k % 2:
        print(k - 2)
    elif (a + b) % 2 != 0:
        print(k - 1)
    else:
        print(k)
