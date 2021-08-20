n = int(input())
a = []
for i in range(n):
    (l, r) = list(map(int, input().split()))
    a.append((l, r))
q = int(input())
k = 0
for i in a:
    if q > i[1]:
        k += 1
print(n - k)
