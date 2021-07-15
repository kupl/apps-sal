S = input()
N = len(S)
cnt = [0 for i in range(N)]
even = 1
odd = 0
prev = 'R'
now = ''
flag1 = 0
flag2 = 0

for i in range(1,N):
    now = S[i]
    if prev != now:
        if prev == 'R':
            flag1 = i-1
            flag2 = i
        else:
            if flag1 % 2 == 0:
                cnt[flag1] = even
                cnt[flag2] = odd
            else:
                cnt[flag2] = even
                cnt[flag1] = odd
            odd = 0
            even = 0
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    prev = now

if flag1 % 2 == 0:
    cnt[flag1] = even
    cnt[flag2] = odd
else:
    cnt[flag2] = even
    cnt[flag1] = odd

print(' '.join([str(a) for a in cnt]))
