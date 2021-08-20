N = int(input())
N_ri = round(pow(N, 1 / 2))
for i in range(N_ri, 0, -1):
    if N % i == 0:
        j = N // i
        break
print(i + j - 2)
