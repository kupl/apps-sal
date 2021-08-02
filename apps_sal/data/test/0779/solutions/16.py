t = int(input())
count = 0
for i in range(1, t):
    if t % i == 0:
        count += 1
print(count)
