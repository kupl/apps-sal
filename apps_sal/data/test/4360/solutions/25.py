n = int(input())
a = list(map(int, input().split()))
x = sum([1/a[i] for i in range(n)])
print(1/x)
