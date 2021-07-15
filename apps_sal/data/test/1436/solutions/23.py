n = int(input())
A = input().split()
c = 0
p = 0
for i in range(n):
    if int(A[i]) > 0:
        p += int(A[i])
    else:
        if p > 0:
            p -= 1
        else:
            c += 1
print(c)
