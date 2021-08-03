N = int(input())
keta = len(str(10 ** 10))
for i in range(1, int(10**5) + 1):
    if N % i == 0:
        keta = min(keta, max(len(str(i)), len(str(N // i))))
print(keta)
