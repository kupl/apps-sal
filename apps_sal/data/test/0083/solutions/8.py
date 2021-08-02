n = int(input())
a = list(map(int, input().split()))

p = sum([1 for i in a if i > 0])
ng = sum([1 for i in a if i < 0])

if p >= n / 2:
    print(1)
elif ng >= n / 2:
    print(-1)
else:
    print(0)
