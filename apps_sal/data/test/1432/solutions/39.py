N = int(input())
A = [int(x) for x in input().split()]

t = 0
for i in range(N):
    if i % 2 == 0:
        t += A[i]
    else:
        t -= A[i]
for a in A:
    print(t, "", end="")
    t = -t + a * 2
print()
