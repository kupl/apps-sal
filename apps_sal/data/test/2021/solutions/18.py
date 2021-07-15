n = int(input())
a = sorted(map(int, input().split()), reverse=True)
m = int(input())
q = [*map(int, input().split())]

t = sum(a)

for i in q:
    print(t - a[i - 1])
