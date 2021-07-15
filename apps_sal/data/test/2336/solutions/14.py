import sys

def main():
    n,k,q=list(map(int,sys.stdin.readline().split()))
    maxtemp=200001
    deltatemp_plus=[0]*maxtemp
    deltatemp_minus=[0]*maxtemp
    for i in range(n):
        li,ri=list(map(int,sys.stdin.readline().split()))
        deltatemp_plus[li]+=1
        deltatemp_minus[ri]+=1
    
    temp=[0]*maxtemp
    cumsum=0
    for i in range(maxtemp):
        cumsum+=deltatemp_plus[i]
        temp[i]=cumsum
        cumsum-=deltatemp_minus[i]
    
    goodtemp=[0]*maxtemp
    goodtemp[0]=1 if temp[0]>=k else 0
    for i in range(1,maxtemp):
        adder=1 if temp[i]>=k else 0
        goodtemp[i]=goodtemp[i-1]+adder
        
    for iq in range(q):
        ai,bi=list(map(int,sys.stdin.readline().split()))
        if ai==0: result=goodtemp[bi]
        else: result=goodtemp[bi]-goodtemp[ai-1]
        sys.stdout.write(str(result)+'\n')
    
main()


