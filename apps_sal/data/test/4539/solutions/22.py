n = input()
n_int = int(n)

n_sum = 0

for s in n:
    n_sum += int(s)

if(n_int%n_sum == 0):
    print("Yes")
else:
    print("No")
