q = int(input())
for i in range(q):
    (x, y, k) = list(map(int, input().split()))
    if max(x, y) > k:
        print(-1)
    elif x == y and k == x + 1:
        print(k - 2)
        continue
    elif x % 2 == 1 and y % 2 == 1 and (k % 2 == 0):
        print(k - 2)
        continue
    elif x % 2 == 0 and y % 2 == 0 and (k % 2 == 1):
        print(k - 2)
        continue
    elif (x + y) % 2 == 0:
        print(k)
    else:
        print(k - 1)
