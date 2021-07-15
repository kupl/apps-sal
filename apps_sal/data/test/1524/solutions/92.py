s = input()
cnt = [0,0]
I = ""
ans = [0] * len(s)
for i in range(len(s)):
    if s[i] == "R": 
        if I == "": cnt[0] += 1
        else:
            ans[I] = (cnt[0]+1)//2 + cnt[1]//2
            ans[I+1] = cnt[0]//2 + (cnt[1]+1)//2
            cnt = [1,0]
            I = ""
    else:
        if I == "": I = i-1
        cnt[1] += 1
ans[I] = (cnt[0]+1)//2 + cnt[1]//2
ans[I+1] = cnt[0]//2 + (cnt[1]+1)//2
print(" ".join(map(str, ans)))
