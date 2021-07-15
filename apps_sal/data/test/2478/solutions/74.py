N = int(input())
S = input()

flg_l = False
cnt_r = 0
cnt_l = 0

for i in range(N):
    if(S[i] == "("):
        cnt_r += 1
        flg_l = True            
    else:
        if(flg_l):
            if(cnt_r > 0):
                cnt_r -= 1
            else:
                cnt_l += 1
                flg_l = False
        else:
            cnt_l += 1
    
ans = ""

ans += ("("*cnt_l)+S+(")"*cnt_r)
print(ans)
