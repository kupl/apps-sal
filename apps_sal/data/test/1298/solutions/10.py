n=int(input())
a=input()
cnt0=0
cnt1=0
for i in range(n):
    if a[i]=='0':
        cnt0+=1
    else:
        cnt1+=1
print(abs(cnt1-cnt0))

