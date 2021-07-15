x = int(input())
y = list(map(int, input().split(' ')))
tot = sum(y)
mod = tot % x
if mod == 0:
    print(x)
else:
    print(x-1)
