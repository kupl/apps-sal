x = list(map(int, input().split()))
for i in range(int(input())):
    x.sort()
    x[-1] = x[-1] * 2
print(sum(x))
