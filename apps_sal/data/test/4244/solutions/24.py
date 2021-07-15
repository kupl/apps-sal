n = int(input())
x = input().split()

min = 2**20

for p in range(100):
    min_i = 0
    if p in x:
        continue
    for i in x:
        min_i = min_i + (int(i) - p)**2
    if min_i <= min:
        min = min_i
print(min)
