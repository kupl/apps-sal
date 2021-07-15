N = int(input())
n = str(N)
Ns = 0
for i in range(len(n)):
    Ns += int(n[i:i+1])
if (Ns % 9) == 0:
    print('Yes')
else:
    print('No')
