N=int(input())
N_26=[]

while N>0:
    N-=1
    N_mod=N%26
    N=N//26
    N_26.append(chr(97+N_mod))
print(("".join(list(reversed(N_26)))))

