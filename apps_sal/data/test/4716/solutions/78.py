n, k = list(map(int, input().split()))
a = [int(i) for i in input().split()]

a.sort(reverse=True)
print((sum(a[:k])))

