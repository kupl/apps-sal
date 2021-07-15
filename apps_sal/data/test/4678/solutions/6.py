N = int(input())
A = list(map(int, input().split()))
A_sub = A[1:]
a_before = A[0]
count = 0
for a in A_sub:
    if a < a_before:
        count += a_before - a
    else:
        a_before = a
print(count)
