n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
p = a[0]
q = sum(a[1:])
r = p - q + 1
print(r)
