b = input().split()
n = int(b[0])
l = int(b[1])

a = input().split()

for i in range(n):
    a[i] = int(a[i])

a = sorted(a)
answer = 0
for i in range(n - 1):
    if a[i + 1] - a[i] > answer:
        answer = a[i + 1] - a[i]

print(max(answer / 2, a[0], l - a[-1]))
