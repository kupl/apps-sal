n = int(input())
t = input().split()
t[0] = int(t[0])
s = t[0] * (n - t[0] + 1)
for i in range(1, n):
    t[i] = int(t[i])
    if t[i] > t[i - 1]:
        s = s + (t[i] - t[i - 1]) * (n - t[i] + 1)
    else:
        s = s + t[i] * (t[i - 1] - t[i])
print(s)
