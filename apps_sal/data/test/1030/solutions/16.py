n, p, k = map(int, input().split())
if p > k + 1:
    print("<<", end=" ")
for i in range(max(1, p - k), min(n, p + k) + 1):
    if i != p:
        print(i, end=" ")
    else:
        print("(", end="")
        print(i, end="")
        print(")", end=" ")
if p < n - k:
    print(">>", end=" ")
