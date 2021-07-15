input()
S = list(map(int,list(input())))
an = 0

for i in range(len(S)):
    if S[i] % 2 == 0:
        an += i + 1
print(an)        

