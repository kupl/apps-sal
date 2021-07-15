n, x = int(input()), list(sorted(list(map(int, input().split()))))

kk = 1

a = 0

for i in range(len(x)):

    a += (x[i] - x[len(x) - i - 1]) * kk

    kk *= 2

    kk %= 1000000007

    a %= 1000000007

print(a)



# Made By Mostafa_Khaled

