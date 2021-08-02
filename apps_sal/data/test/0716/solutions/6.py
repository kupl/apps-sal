n, a, b = map(int, input().split())
k = input()
if k[a - 1] == k[b - 1]:
    print(0)
else:
    print(1)
