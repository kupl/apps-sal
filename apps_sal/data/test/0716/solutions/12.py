(n, a, b) = map(int, input().split())
lst = input()
if lst[a - 1] == lst[b - 1]:
    print(0)
else:
    print(1)
