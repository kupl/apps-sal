# cook your dish here
s = input()
ln = len(s)
ai = 100000
bi= 100000
ci= 100000
bj = -100000
aj=-100000
cj = -1000000
for i in range(ln):
    if(s[i]=='a'):
        #print('a found')
        if(ai>i):
            ai= i
        if(aj<i):
            aj= i
    if(s[i]=='b'):
        #print("bfound")
        if(bi>i):
            bi= i
        if(bj<i):
            bj= i
    if(s[i]=='c'):
        #print("c found")
        if(ci>i):
            ci= i
        if(cj<i):
            cj= i
lst = [abs(ai-bj),abs(ai-cj),abs(bi-aj),abs(ci-aj),abs(bi-cj),abs(ci-bj)]
mxm = -1
for i in lst:
    if(i<ln):
        if(mxm<i):
            mxm=i
print(mxm)
