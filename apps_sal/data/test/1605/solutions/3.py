cnt = [[0 for col in range(2)] for row in range(2)]
ans = [0 for col in range(2)]
strx = input()
length = len(strx)
for i in range(length):
    if(strx[i]=='a'):
        cnt[0][i & 1]=cnt[0][i & 1]+1
        ans[0]+=cnt[0][i & 1 ^ 1]
        ans[1]+=cnt[0][i & 1]
    else:
        cnt[1][i & 1]=cnt[1][i & 1]+1
        ans[0]+=cnt[1][i & 1 ^ 1]
        ans[1]+=cnt[1][i & 1]
print(ans[0],ans[1])

