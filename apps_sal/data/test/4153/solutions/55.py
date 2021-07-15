s=input()
cnt0 = 0
cnt1 = 0
for i in s:
    if i == '0':
        cnt0 +=1
    else:
        cnt1 +=1

print(2*min(cnt0,cnt1))
