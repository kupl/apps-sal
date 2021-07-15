S = input()
ans = []
for i in range(len(S)-2):
    chk = int(S[i]+S[i+1]+S[i+2])
    if chk == 753:
        print((0))
        return
    else:
        ans.append(abs(753-chk))
ans = sorted(ans)
print((ans[0]))
pass

