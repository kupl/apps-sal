H, N = map(int, input().split())

A = list(map(int, input().split()))
sum_A = sum(A)

if H <= sum_A:
    print("Yes")
else:
    print("No")
