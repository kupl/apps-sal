n = int(input())
seq = input()
nbPaires = 0
for i in range(n):
    if int(seq[i]) % 2 == 0:
        nbPaires += i + 1
print(nbPaires)
