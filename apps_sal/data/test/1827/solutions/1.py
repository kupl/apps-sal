n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    b = max(a)
    c = min(a)
    print(b, c)
    a.remove(b)
    a.remove(c)
