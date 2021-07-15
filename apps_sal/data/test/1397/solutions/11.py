n, m = list(map(int, input().split()))
print(n - 1)
t = []
for i in range(m): 
    t += input().split()
t = set(t)
i = 1
while str(i) in t: i += 1
for j in range(1, i):
    print(i, j)
for j in range(i + 1, n + 1):
    print(i, j)

