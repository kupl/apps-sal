S = input()
for i in range(len(S)):
    S = S[0:len(S)-1]
    if(len(S) % 2 == 0):
        if((S[0:(len(S)//2)]) == (S[(len(S)//2):len(S)+1])):
            print(str(len(S)))
            return
