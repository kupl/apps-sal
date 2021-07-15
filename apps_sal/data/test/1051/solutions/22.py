k = int(input())
a = list(map(int, input().split()))
c = max(a)
if c <= 25:
    print(0)
else:
    print(c - 25)

