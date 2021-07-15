n = int(input())
t = 0
for i in range(n):
    if len(str(i + 1)) % 2 == 1:
        t += 1
print(t)

