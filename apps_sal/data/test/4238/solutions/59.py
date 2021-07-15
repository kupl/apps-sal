N = input()
sum_N = 0

for i in range(len(N)):
    sum_N = (sum_N + int(N[i])) % 9

if sum_N == 0:
    print("Yes")
else:
    print("No")
