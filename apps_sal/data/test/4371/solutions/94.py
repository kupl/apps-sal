N=int(input())
def ans114(N:int):
    answer = 0
    N=str(N)
    while len(N)>=3:
        N2=int(N[0]+N[1]+N[2])
        if abs(753-N2)<abs(answer-753):
            answer=N2
            N=N[1:]
        else:
            N=N[1:]
    return abs(753-answer)
print(ans114(N))
