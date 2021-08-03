N_string = input()
N = int(N_string)
sum = 0
for n in N_string:
    sum = sum + int(n)
if N % sum == 0:
    print('Yes')
else:
    print('No')
