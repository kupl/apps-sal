a, b = map(int, input().split())
m = b - a # [m-1] と [m]
t = 0
for i in range(m):
  t += i
print(t - a)
