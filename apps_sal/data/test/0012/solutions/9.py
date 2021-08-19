n = int(input())
s = str(input())
last_seq = 0
curr_seq = 0
ans = 0
gcount = 0
i = 0
while i < n - 1:
    if s[i] == 'G':
        gcount += 1
        curr_seq += 1
        i += 1
    else:
        if curr_seq + last_seq > ans:
            ans = curr_seq + last_seq
        if s[i + 1] == 'G':
            # gcount+=1
            last_seq = curr_seq
            curr_seq = 0
            i += 1
        else:
            if curr_seq > ans:
                ans = curr_seq
            curr_seq = 0
            last_seq = 0
            i += 2
if s[-1] == 'G':
    gcount += 1
    curr_seq += 1
if curr_seq + last_seq > ans:
    ans = curr_seq + last_seq
# print(gcount,ans)
if gcount > ans:
    print(ans + 1)
else:
    print(ans)
