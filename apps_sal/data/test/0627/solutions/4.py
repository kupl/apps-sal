n = int(input())
t = input()
for i in range(n - 1):
    if t[i] > t[i + 1]:
        t = t[:i] + t[i + 1:]
        break
if len(t) == n:
    print(t[:n - 1])
else:
    print(t)
