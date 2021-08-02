a = sorted(list(map(int, input().split())))
m = a.pop()
for i in range(int(input())):
    m *= 2
print(sum(a) + m)
