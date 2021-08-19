"""
def main():
	from sys import stdin,stdout
def __starting_point():
	main()
"""
"\ndef main():\n\tfrom sys import stdin,stdout\n\tN = int(stdin.readline())\n\tarr = list(map(int,stdin.readline().split()))\n\tdiv = []\n\tfor i in arr:\n\t\tdiv.append(N//i)\n\tmaxim = 0\n\tmaxindex = -1\n\tfor i in range(9):\n\t\tif div[i] >maxim:\n\t\t\tmaxim = div[i]\n\t\t\tmaxindex = i\n\tif maxindex > -1:\n\t\tans = [ (maxindex+1) for i in range(maxim)]\n\t\tN= N%arr[maxindex]\n\t\t#print(N)\n\t\ti = 0\n\t\twhile i<maxim:\n\t\t\t#print('i=',i,'N=',N)\n\t\t\tfor j in range(8,maxindex,-1):\n\t\t\t\t#print('j=',j,'diff=',arr[j]-arr[ans[i]-1])\n\t\t\t\tif arr[j]-arr[ans[i]-1] <=N:\n\t\t\t\t\tN -= arr[j]-arr[ans[i]-1]\n\t\t\t\t\tans[i] = j+1\n\t\t\t\t\tbreak\n\t\t\ti+=1\n\t\tfor i in ans:\n\t\t\tstdout.write(str(i))\n\telse:\n\t\tstdout.write('-1\n')\ndef __starting_point():\n\tmain()\n"


def main():
    from sys import stdin, stdout
    import collections
    with open('input.txt', 'r') as ip:
        (N, K) = list(map(int, ip.readline().split()))
        arr = list(map(int, ip.readline().split()))
    mydict = collections.defaultdict(set)
    for i in range(len(arr)):
        mydict[arr[i]].add(i + 1)
    ans = []
    i = 0
    while K > 0:
        for it in mydict[sorted(list(mydict.keys()), reverse=True)[i]]:
            ans.append(it)
            K -= 1
            if K < 1:
                break
        minim = i
        i += 1
    with open('output.txt', 'w') as out:
        out.write(str(sorted(list(mydict.keys()), reverse=True)[minim]) + '\n')
        ans = ' '.join((str(x) for x in ans))
        out.write(ans + '\n')


def __starting_point():
    main()


__starting_point()
