A = list(map(int, input().split()))
su = sum(A)



for i in range(2**4):
    a1 = 0
    for j in range(4):
        if i >> j & 1:
            a1 += A[j]


    if a1 == su - a1:
        print("Yes")
        return

print("No")
