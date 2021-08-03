n, k = map(int, input().split())
t = input()
for i in range(n - 1):
    if t[i + 1:n] == t[0:n - i - 1]:
        print(t + (k - 1) * t[n - i - 1:n])
        break
else:
    print(k * t)
