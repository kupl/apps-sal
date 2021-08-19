(n, k) = map(int, input().split())
a = list(map(int, input().split()))
s = 0
rec = [0]
for i in range(len(a)):
    rec.append(rec[-1] + a[i])
for i in range(n - k + 1):
    s += rec[i + k] - rec[i]
print(s / (n - k + 1))
