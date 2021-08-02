H, N = map(int, input().split())
A = map(int, input().split())
if H <= sum(A):
    print("Yes")
else:
    print("No")
