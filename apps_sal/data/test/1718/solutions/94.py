(n, k) = list(map(int, input().split()))
_ = input()
l = n - k
x = (l + (k - 1 - 1)) // (k - 1)
print(x + 1)
