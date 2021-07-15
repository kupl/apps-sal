N = int(input())

f = 0

str_N = str(N)

for i in str_N:
    f += int(i)

if N % f == 0:
    print("Yes")
else :
    print("No")
