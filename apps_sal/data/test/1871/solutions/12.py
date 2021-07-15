_, x = list(map(int, input().split()))
c = sorted(list(map(int, input().split())))
r = 0
for i in c:
    r += i*x
    x = max(1, x-1)
print(r)


