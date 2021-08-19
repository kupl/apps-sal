n = int(input())
(*A,) = map(int, input().split())
even = 0
odd = 0
S = 0
for (i, a) in enumerate(A):
    S += a
    if i % 2 == 0 and S <= 0:
        even += -S + 1
        S = 1
    elif i % 2 == 1 and S >= 0:
        even += S + 1
        S = -1
S = 0
for (i, a) in enumerate(A):
    S += a
    if i % 2 == 0 and S >= 0:
        odd += S + 1
        S = -1
    elif i % 2 == 1 and S <= 0:
        odd += -S + 1
        S = 1
print(min(even, odd))
