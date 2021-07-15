n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in sorted(a)[::-1]:
    if (k % i == 0):
        print(k // i)
        break

