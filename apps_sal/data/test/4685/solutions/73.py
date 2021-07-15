a = list(map(int, input().split()))
k = int(input())
a.sort(reverse=True)
a[0] *= 2**k
print(sum(a))
