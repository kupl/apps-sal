n = int(input())
a = list(map(int, input().split()))
x = max(a)
print(sum([x - a[i] for i in range(n)]))
