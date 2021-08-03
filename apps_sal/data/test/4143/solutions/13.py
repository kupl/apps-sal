n = int(input())
a = []
for i in range(5):
    a.append(int(input()))
x = min(a)
t = n // x
if n % x != 0:
    t += 1
t += 4
print(t)
