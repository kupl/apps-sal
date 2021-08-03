s = input().split()
n, k = int(s[0]), int(s[1])
t = k // n
if n * t == k:
    print(t)
else:
    print(t + 1)
