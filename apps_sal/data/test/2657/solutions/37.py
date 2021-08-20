n = int(input())
list_A = list(map(int, input().split()))
m = max(list_A)
(r, k) = (0, 0)
for a in list_A:
    if min(m - a, a) > k:
        r = a
        k = min(m - a, a)
print(m, r)
