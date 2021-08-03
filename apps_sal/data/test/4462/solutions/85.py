import collections
_ = input()
A = collections.Counter(int(T) for T in input().split()).most_common()
Num4 = sum(A[T][1] for T in range(0, len(A)) if A[T][0] % 4 == 0)
Num2 = sum(A[T][1] for T in range(0, len(A)) if A[T][0] % 4 != 0 and A[T][0] % 2 == 0)
Odd = sum(A[T][1] for T in range(0, len(A)) if A[T][0] % 2 != 0)
if Num2 > 0:
    Capacity = Num4
else:
    Capacity = Num4 + 1
if Capacity >= Odd:
    print('Yes')
else:
    print('No')
