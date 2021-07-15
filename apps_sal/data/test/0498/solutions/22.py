n, m, k = list(map(int, input().split()))
k2 = ((k - 1) // 2 + 1)
ans2  =k2 % m
if ans2 == 0:
    ans2 = m
print((k2 - 1) // m + 1, ans2, end=" ")
if k % 2 == 1:
    print("L")
else:
    print("R")

