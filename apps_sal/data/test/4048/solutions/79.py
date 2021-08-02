N = int(input())
x = int(N**0.5) + 1
ans_1 = N

for i in range(x):
    if N % x == 0:
        ans_1 = x
        break
    else:
        x -= 1

ans_2 = N // ans_1
print((ans_1 + ans_2 - 2))
