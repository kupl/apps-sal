S = input()

#print ((len(S)-1)//2)
#print ((len(S)+3)//2)
#print (S[0:(len(S)-1)//2])
#print (S[((len(S)+3)//2)-1:len(S)])
#print (S[::-1])

Skai1 = S[0:(len(S) - 1) // 2]
Skai1 = Skai1[::-1]
Skai2 = S[((len(S) + 3) // 2) - 1:len(S)]
Skai2 = Skai2[::-1]

if S == S[::-1] and S[0:(len(S) - 1) // 2] == Skai1 and S[((len(S) + 3) // 2) - 1:len(S)] == Skai2:
    print('Yes')
else:
    print("No")
