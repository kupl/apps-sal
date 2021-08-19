N = int(input())
Sn = 0
i = str(N)
for n in range(len(i)):
    Sn += int(i[n])
print('Yes' if N % Sn == 0 else 'No')
