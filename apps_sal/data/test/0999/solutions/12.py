n = int(input())
mr = 10 ** 10
ml2 = 0
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    mr = min(mr, b)
    ml2 = max(ml2, a)
ml = 0
mr2 = 10 ** 10
n = int(input())
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    ml = max(ml, a)
    mr2 = min(mr2, b)
print(max(0, ml - mr, ml2 - mr2))
