N = int(input())
n = N % 11
K = N // 11 * 2
if n == 0:
    pass
elif 0 < n <= 6:
    K += 1
else:
    K += 2
print(K)
