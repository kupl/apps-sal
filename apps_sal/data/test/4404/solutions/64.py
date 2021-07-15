S = list(input())
y = 1000*int(S[0])+100*int(S[1])+10*int(S[2])+int(S[3])
m = 10*int(S[5])+int(S[6])
d = 10*int(S[8])+int(S[9])

if y < 2019 :
    print("Heisei")
elif y == 2019 and m <= 4 :
    print("Heisei")
else :
    print("TBD")

