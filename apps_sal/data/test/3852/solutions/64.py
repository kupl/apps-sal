n = int(input())
a = list(map(int, input().split()))
print(n * 2 - 1)
ma, mi = max(a), min(a)
ima, imi = a.index(ma), a.index(mi)
if abs(ma) >= abs(mi):
    for i in range(1, n + 1):
        print(ima + 1, i)
    for i in range(1, n):
        print(i, i + 1)
else:
    for i in range(1, n + 1):
        print(imi + 1, i)
    for i in range(1, n)[::-1]:
        print(i + 1, i)
