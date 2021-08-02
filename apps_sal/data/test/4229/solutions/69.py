N = int(input())
N_sum = 0
for i in range(N + 1):
    if i % 3 != 0 and i % 5 != 0:
        N_sum += i
print(N_sum)
