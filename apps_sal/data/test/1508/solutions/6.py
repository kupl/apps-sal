n = int(input())
A = list(map(int, input().split()))
Max = max(A)
Min = min(A)
ind1 = A.index(Max)
A.pop(ind1)
ind2 = A.index(Min)
A.pop(ind2)
if len(A) > 0:
    print(str(Max), ' '.join(map(str, sorted(A))), str(Min))
else:
    print(str(Max), str(Min))
