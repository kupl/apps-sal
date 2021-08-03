n = int(input())
y = [int(x) for x in input().split()]
y.sort()
a = y[:int(n / 2)]
b = y[int(n / 2):]
print(sum(a)**2 + sum(b)**2)
