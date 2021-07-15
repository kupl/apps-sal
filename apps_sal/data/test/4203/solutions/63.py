S=input()
k=0
z=0
cnt=0
if S[0]=='A':
    for i in range(2,len(S)-1):
        if S[i]=='C':
            k=i
            cnt += 1
            z=100
            if z==100 and cnt==1:
                for j in range(1,k):
                    if 'a'<=S[j]<='z':
                        z=200
                    else:
                        print('WA')
                        return
                if z==200 :        
                    for l in range(k+1,len(S)):
                        if 'a'<=S[l]<='z':
                            z=102
                        else:
                            print('WA')
                            return
if z == 0 or z==100:
    print('WA')
else:
    print('AC')
