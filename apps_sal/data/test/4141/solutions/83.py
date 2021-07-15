N = int(input())
A = list(map(int, input().split()))
j = 0
k = 0
for i in A:
    if i % 2 == 0:
        k = k + 1
        if i % 3 == 0:
            j = j + 1
        elif i % 5 == 0:
            j = j + 1


if k == j:
    print("APPROVED")
else:
    print("DENIED")
