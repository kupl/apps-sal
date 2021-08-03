_, k = list(map(int, input().split()))
A = [*[int(x) - 1 for x in input().split()]]
ng, ok = 0, 1 << 30
while ok - ng > 1:
    m = (ng + ok) // 2
    if k < sum(a // m for a in A):
        ng = m
    else:
        ok = m
print(ok)
