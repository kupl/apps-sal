N=int(input())

def ans111(N:int):
    while N<=999:
        if str(N)[0]==str(N)[1]==str(N)[2]:
            break
        else:
            N+=1
    return N

print(ans111(N))
