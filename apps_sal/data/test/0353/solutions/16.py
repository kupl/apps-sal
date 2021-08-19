"""
def main():
    from sys import stdin,stdout
def __starting_point():
    main()
"""
'\ndef main():\n    from sys import stdin,stdout\n    n,c=map(int,stdin.readline().split())\n    tup=tuple(map(int,stdin.readline().split()))\n    counter=1\n    for i in range(1,n):\n        if tup[i]-tup[i-1]<=c:\n            counter+=1\n        else:\n            counter=1\n    stdout.write(str(counter))\ndef __starting_point():\n    main()\n'
"\ndef main():\n    from sys import stdin,stdout\n    s=stdin.readline().strip().lower()\n    dic={}\n    qcounter=0\n    for i in 'qwertyuiopasdfghjklzxcvbnm':\n        dic[i]=0\n    if len(s)<26:\n        stdout.write('-1')\n    else:\n        for i in s:\n            if i=='?':\n                qcounter+=1\n            else:\n                dic[i]+=1\n        l=[]\n        x=list(dic.values()).count(0)\n        if qcounter==26 and x==26:\n            stdout.write('qwertyuiopasdfghjklzxcvbnm'.upper())\n        elif x==0 and qcounter==0:\n            stdout.write(s.upper())\n        elif qcounter>=x:\n            for i in 'qwertyuiopasdfghjklzxcvbnm':\n                if dic[i]==0:\n                    l.append(i.upper())\n            m=len(l)\n            i=0\n            t=''\n            for j in range(len(s)):\n                if s[j]=='?':\n                    if i>=m:\n                        i=0\n                    t=t[:j]+l[i]\n                    i+=1\n                else:\n                    t+=s[j].upper()\n            stdout.write(t)\n        else:\n            stdout.write('-1')\ndef __starting_point():\n    main()\n"


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
    elif tup[-1] - tup[-2] > 0:
        if tup[-1] == 15:
            stdout.write('DOWN')
        else:
            stdout.write('UP')
    elif tup[-1] == 0:
        stdout.write('UP')
    else:
        stdout.write('DOWN')


def __starting_point():
    main()


__starting_point()
