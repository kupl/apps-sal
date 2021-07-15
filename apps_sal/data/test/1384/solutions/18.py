n = int(input())
a = list(map(int, input().split()))
l = [a[i+1:].count(0)+a[:i].count(1) for i in range(n)]
print(n - min(l))
