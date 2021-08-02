H, N, *A = map(int, open(0).read().split())
print("Yes") if H <= sum(A) else print("No")
