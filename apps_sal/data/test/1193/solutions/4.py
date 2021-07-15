n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted(a,reverse=True)
a = a[:k]
print(a[-1])

