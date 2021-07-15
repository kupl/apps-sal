A, B =list(map(int, input().split()))
num_palin = [0] * (B+1)
for i in range(1,B+1):
    if str(i) == str(i)[::-1]:
        num_palin[i] = num_palin[i-1] + 1
    else:
        num_palin[i] = num_palin[i-1]
print((num_palin[B]-num_palin[A-1]))

