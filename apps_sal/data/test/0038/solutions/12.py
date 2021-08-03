

n, l = list(map(int, input().split()))
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


first_diff = A[0]
A = [x - first_diff for x in A]

first_diff = B[0]
B = [x - first_diff for x in B]

found = False

for _ in range(n + 2):
    if A == B:
        found = True

    B = B[1:] + [B[0] + l]
    first_diff = B[0]
    B = [x - first_diff for x in B]


if found:
    print("YES")
else:
    print("NO")
