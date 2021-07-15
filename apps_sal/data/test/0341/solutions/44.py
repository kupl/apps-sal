N,K = list(map(int, input().split()))
R,S,P = list(map(int, input().split()))
T = input()

score_list = []

ans = 0
for i in range(K):
    pre_word = "dummy"
    for j in range(i,N,K):
        if(T[j] != pre_word):
            if(T[j] == "r"):
                ans += P
                pre_word = "r"
            elif(T[j] == "s"):
                ans += R
                pre_word = "s"
            else:
                ans += S
                pre_word = "p"
        else:
            pre_word = "dummy"
        

print(ans)
