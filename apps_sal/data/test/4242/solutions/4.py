A, B, K = map(int, input().split())
lst = []
for n in range(1, min(A, B)+1):
    if B % n == 0:
        lst.append(n)
lst2 = []
for m in lst:
    if A % m == 0:
        lst2.append(m)
print(sorted(lst2, reverse=True)[K-1])
