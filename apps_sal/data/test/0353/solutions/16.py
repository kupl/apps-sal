'''
def main():
    from sys import stdin,stdout
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    n,c=map(int,stdin.readline().split())
    tup=tuple(map(int,stdin.readline().split()))
    counter=1
    for i in range(1,n):
        if tup[i]-tup[i-1]<=c:
            counter+=1
        else:
            counter=1
    stdout.write(str(counter))
def __starting_point():
    main()
'''
'''
def main():
    from sys import stdin,stdout
    s=stdin.readline().strip().lower()
    dic={}
    qcounter=0
    for i in 'qwertyuiopasdfghjklzxcvbnm':
        dic[i]=0
    if len(s)<26:
        stdout.write('-1')
    else:
        for i in s:
            if i=='?':
                qcounter+=1
            else:
                dic[i]+=1
        l=[]
        x=list(dic.values()).count(0)
        if qcounter==26 and x==26:
            stdout.write('qwertyuiopasdfghjklzxcvbnm'.upper())
        elif x==0 and qcounter==0:
            stdout.write(s.upper())
        elif qcounter>=x:
            for i in 'qwertyuiopasdfghjklzxcvbnm':
                if dic[i]==0:
                    l.append(i.upper())
            m=len(l)
            i=0
            t=''
            for j in range(len(s)):
                if s[j]=='?':
                    if i>=m:
                        i=0
                    t=t[:j]+l[i]
                    i+=1
                else:
                    t+=s[j].upper()
            stdout.write(t)
        else:
            stdout.write('-1')
def __starting_point():
    main()
'''


def main():
    from sys import stdin, stdout
    n = int(stdin.readline())
    tup = tuple(map(int, stdin.readline().split()))
    if n == 1:
        if tup[0] == 0:
            stdout.write('UP')
        elif tup[0] == 15:
            stdout.write('DOWN')
        else:
            stdout.write('-1')
    else:
        if tup[-1] - tup[-2] > 0:
            if tup[-1] == 15:
                stdout.write('DOWN')
            else:
                stdout.write('UP')
        else:
            if tup[-1] == 0:
                stdout.write('UP')
            else:
                stdout.write('DOWN')


def __starting_point():
    main()


__starting_point()
