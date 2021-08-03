a = int(input())
b = list(map(int, input().split()))
b.sort()
if b[(a // 2)] == b[(a // 2 - 1)]:
    print((0))
else:
    print((b[(a // 2)] - b[(a // 2 - 1)]))
