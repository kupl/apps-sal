N = int(input())
num = 0

for i in range(1, N + 1):
    if len(str(i)) % 2 == 1:
        num += 1
print(num)
