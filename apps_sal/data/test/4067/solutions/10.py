N=int(input())
S=list(input())
Zero, One, Two = S.count("0"), S.count("1"), S.count("2")

i = 0
while i < N and Zero < N//3:
    if S[i] == "1" and One > N//3:
        S[i] = "0"
        Zero+=1
        One-=1
    elif S[i] == "2" and Two > N//3:
        S[i] = "0"
        Zero+=1
        Two-=1
    i += 1

i = N - 1
while i >= 0 and Two < N//3:
    if S[i] == "0" and Zero > N//3:
        S[i] = "2"
        Two += 1
        Zero -= 1
    elif S[i] == "1" and One > N//3:
        S[i] = "2"
        Two += 1
        One -= 1
    i-=1

i = 0
while i < N and One < N//3:
    if S[i] == "2" and Two > N//3:
        S[i] = "1"
        One += 1
        Two -= 1
    i+=1

i = N - 1
while i >= 0 and One < N//3:
    if S[i] == "0" and Zero > N//3:
        S[i] = "1"
        One += 1
        Zero -= 1
    i-=1



print("".join(S))   
