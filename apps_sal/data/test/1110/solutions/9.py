N = int(input())
step = 1
S = 0
while step <= N:
    S = S + step * (N - step) + 1
    step = step + 1
print(S)
