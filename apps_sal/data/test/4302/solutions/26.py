(A, B) = list(map(int, input().split()))
count = 0
for i in range(0, 2):
    if A == B:
        count = count + A
    elif A > B:
        count = count + A
        A = A - 1
    elif A < B:
        count = count + B
        B = B - 1
print(count)
