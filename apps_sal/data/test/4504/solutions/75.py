S = list(input())

for i in range(2, len(S)):
    miniS = S[0:-i]
    if len(miniS) % 2 == 0:
        front = ''.join(miniS[0:len(miniS)//2])
        back = ''.join(miniS[len(miniS)//2:len(miniS)])
        if front == back:
            print(len(miniS))
            return
