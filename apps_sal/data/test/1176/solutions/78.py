n = int(input())
A = list(map(int, input().split()))
cnt = sum([0 if a > 0 else 1 for a in A])
absA = sorted([abs(a) for a in A])
if cnt % 2 == 1:
    print(sum(absA) - 2 * absA[0])
else:
    print(sum(absA))
