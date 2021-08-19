N = int(input())
b_num = 0
for a in range(1, N):
    if N % a == 0:
        b_num += int(N / a) - 1
    else:
        b_num += N // a
print(b_num)
