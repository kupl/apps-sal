N=int(input());A=list(map(int,input().split()));print("ADPEPNRIOEVDE D"[any(a%2*8-a%3*a%5<0for a in A)::2])
