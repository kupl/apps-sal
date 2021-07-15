n = int(input())
a = list(map(int, input().split()))

even = 0
for i in range(n):
    if a[i] % 2 == 0:
        even += 1

if even == 0 or even == n:
    pass
else:
    a.sort()

print(" ".join(map(str, a)))

