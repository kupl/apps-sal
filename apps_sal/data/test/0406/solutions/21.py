I = lambda : map(int,input().split())
n = int(input())
p = list(I())
cnt = [0] * 1000001
for i in p: cnt[i] += 1
for i in range(1000000,1,-1):
    if cnt[i] % 2 == 1 and cnt[i - 1] > 0:
        cnt[i] -= 1
        cnt[i - 1] += 1
    elif cnt[i] % 2 == 1 and cnt[i - 1] == 0:
        cnt[i] -= 1
p = 0
ans = 0
for i in range(1000000,1,-1):
    if cnt[i] != 0:
        if p != 0:
            cnt[i] -= 2
            ans += p * i
            p = 0
        ans += i * i * (cnt[i] // 4)
        if cnt[i] % 4 != 0:
            p = i
print (ans)
