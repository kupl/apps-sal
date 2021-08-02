N = int(input())
dna = input()

A_num = 0
C_num = 0
G_num = 0
T_num = 0

for i in range(N):
    if dna[i] == 'A':
        A_num += 1

    elif dna[i] == 'C':
        C_num += 1

    elif dna[i] == 'T':
        T_num += 1

    else:
        G_num += 1

numbers = [A_num, C_num, G_num, T_num]

numbers.sort(key=lambda x: -x)

if numbers[0] > numbers[1]:
    print(1)

elif numbers[1] > numbers[2]:
    print(pow(2, N, 1000000007))

elif numbers[2] > numbers[3]:
    print(pow(3, N, 1000000007))

else:
    print(pow(4, N, 1000000007))
