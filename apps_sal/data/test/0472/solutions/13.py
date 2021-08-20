"""
def main():
	from sys import stdin,stdout
def __starting_point():
	main()
"""
"\ndef main():\n\tfrom sys import stdin,stdout\n\tN = int(stdin.readline())\n\tarr = list(map(int,stdin.readline().split()))\n\tdiv = []\n\tfor i in arr:\n\t\tdiv.append(N//i)\n\tmaxim = 0\n\tmaxindex = -1\n\tfor i in range(9):\n\t\tif div[i] >maxim:\n\t\t\tmaxim = div[i]\n\t\t\tmaxindex = i\n\tif maxindex > -1:\n\t\tans = [ (maxindex+1) for i in range(maxim)]\n\t\tN= N%arr[maxindex]\n\t\t#print(N)\n\t\ti = 0\n\t\twhile i<maxim:\n\t\t\t#print('i=',i,'N=',N)\n\t\t\tfor j in range(8,maxindex,-1):\n\t\t\t\t#print('j=',j,'diff=',arr[j]-arr[ans[i]-1])\n\t\t\t\tif arr[j]-arr[ans[i]-1] <=N:\n\t\t\t\t\tN -= arr[j]-arr[ans[i]-1]\n\t\t\t\t\tans[i] = j+1\n\t\t\t\t\tbreak\n\t\t\ti+=1\n\t\tfor i in ans:\n\t\t\tstdout.write(str(i))\n\telse:\n\t\tstdout.write('-1\n')\ndef __starting_point():\n\tmain()\n"
"\ndef main():\n\tfrom sys import stdin,stdout\n\timport collections\n\twith open('input.txt','r') as ip:\n\t\tN,K = map(int,ip.readline().split())\n\t\tarr = list(map(int,ip.readline().split()))\n\tmydict = collections.defaultdict(set)\n\tfor i in range(len(arr)):\n\t\tmydict[arr[i]].add(i+1)\n\tans = []\n\ti=0\n\twhile K>0:\n\t\tfor it in mydict[sorted(mydict.keys(),reverse=True)[i]]:\n\t\t\tans.append(it)\n\t\t\tK-=1\n\t\t\tif K<1:\n\t\t\t\tbreak\n\t\tminim=i\n\t\ti+=1\n\twith open('output.txt','w') as out:\n\t\tout.write(str(sorted(mydict.keys(),reverse=True)[minim])+'\n')\n\t\tans=' '.join(str(x) for x in ans)\n\t\tout.write(ans+'\n')\t\t\ndef __starting_point():\n\tmain()\n"
"\ndef main():\n\tfrom sys import stdin,stdout\n\timport collections\n\tnames = collections.defaultdict(list)\n\tcounter = 0\n\torder = {}\n\tfor i in range(int(stdin.readline())):\n\t\tn,ns = stdin.readline().split()\n\t\tnames[ns]=[0,0,0]\n\t\torder[ns]=counter\n\t\tcounter+=1\n\t\tn=int(n)\n\t\twhile n:\n\t\t\tip=stdin.readline().strip()\n\t\t\tip=ip.replace('-','')\n\t\t\t#test for taxi\n\t\t\tflag=True\n\t\t\tfor i in range(1,6):\n\t\t\t\tif ip[i]!=ip[0]:\n\t\t\t\t\tflag=False\n\t\t\t\t\tbreak\n\t\t\tif flag:\n\t\t\t\tnames[ns][0]+=1\n\t\t\t\tn-=1\n\t\t\t\tcontinue\n\t\t\t#test for pizza\n\t\t\tflag = True\n\t\t\tfor i in range(1,6):\n\t\t\t\tif int(ip[i])>=int(ip[i-1]):\n\t\t\t\t\tflag =False\n\t\t\t\t\tbreak\n\t\t\tif flag:\n\t\t\t\tnames[ns][1]+=1\n\n\t\t\telse:\n\t\t\t\tnames[ns][2]+=1\n\t\t\tn-=1\n\t#print(names)\n\t#for all girls\n\tt=-1\n\tp=-1\n\tg=-1\n\tfor i in names:\n\t\tt=max(t,names[i][0])\n\t\tp = max(p, names[i][1])\n\t\tg = max(g, names[i][2])\n\n\ttaxi=list(filter(lambda x: names[x][0]==t, names.keys()))\n\tpizza = list(filter(lambda x: names[x][1] == p, names.keys()))\n\tgirls = list(filter(lambda x: names[x][2] == g, names.keys()))\n\n\tpizza.sort(key= lambda x: order[x])\n\ttaxi.sort(key= lambda x: order[x])\t\n\tgirls.sort(key= lambda x: order[x])\n\n\tprint('If you want to call a taxi, you should call:',', '.join(x for x in taxi),end='.\n')\n\tprint('If you want to order a pizza, you should call:', ', '.join(x for x in pizza),end='.\n')\n\tprint('If you want to go to a cafe with a wonderful girl, you should call:', ', '.join(x for x in girls),end='.\n')\n\ndef __starting_point():\n\tmain()\n"
'\ndef LCMgen(a):\n\timport math\n\tlcm = a[0]\n\tfor i in range(1,len(a)):\n\t\tg = math.gcd(lcm,a[i])\n\t\tlcm = (lcm*a[i])//g\n\treturn lcm\t\n\t\ndef main():\n\tfrom sys import stdin,stdout\n\timport collections\n\timport math\n\tN,W = map(int,stdin.readline().split())\n\tcounter = collections.Counter(map(int,stdin.readline().split()))\n\tlcm = LCMgen(list(counter.keys()))\n\tW*=lcm\n\tdiv = 0\n\tfor i in counter:\n\t\tdiv+=counter[i]*(lcm//i)\n\tans = math.ceil(W/div)\n\tstdout.write(str(ans))\ndef __starting_point():\n\tmain()\n'
"\ndef main():\n    from sys import stdin,stdout\n    ip = stdin.readline().strip()\n    inte = None\n    flow = None\n    for i,j in enumerate(ip):\n        if j=='.':\n            flow = ip[i:]\n            inte = ip[:i]\n            break\n    if flow == None:\n        flow = '.00'\n        inte = ip\n    else:\n        if len(flow)==2:\n            flow+='0'\n        else:\n            flow = flow[:3]\n    ne = False\n    if ip[0]=='-':\n        ne = True\n    if ne:\n        inte = inte[1:]\n    inte = inte[::-1]\n    ans =''\n    for i,j in enumerate(inte):\n        ans += j\n        if i%3 == 2:\n            ans+=','\n    ans = ans[::-1]\n    if ans[0]==',':\n        ans = ans[1:]\n    ans = '$'+ans\n    if ne:\n        stdout.write('({})'.format(ans+flow))\n    else:\n        stdout.write(ans+flow)\ndef __starting_point():\n    main()\n\n"
'\ndef main():\n    from sys import stdin,stdout\n    n = int(stdin.readline())\n    arr = list(map(int,stdin.readline().split()))\n    minim = min(arr)\n    my_l = []\n    for i,j in enumerate(arr):\n        if j==minim:\n            my_l.append(i)\n    my_l_ = []\n    for i in range(1,len(my_l)):\n        my_l_.append(my_l[i]-my_l[i-1])\n    stdout.write(str(min(my_l_)))\ndef __starting_point():\n    main()\n'
'\ndef main():\n    from sys import stdin,stdout\n    n,a,b = map(int,stdin.readline().split())\n    maxim = -1\n    for i in range(1,n):\n        maxim = max(min(a//i,b//(n-i)),maxim)\n    stdout.write(str(maxim))\ndef __starting_point():\n    main()\n'
"\ndef main():\n    from sys import stdin,stdout\n    def foo(x):\n        tsum = 0\n        c = x\n        while c:\n            tsum+=(c%10)\n            c//=10\n        return tsum\n\n    N = int(stdin.readline())\n    up,down = 0 , int(1e18)\n    flag = False\n    while up<down:\n        mid = (up+down)//2\n        val = foo(mid)\n        val = (mid+val)*mid\n        if val<N:\n            up = mid\n        elif val >N:\n            down = mid\n        else:\n            flag=True\n            break\n        \n    if flag:\n        stdout.write(str(mid)+'\n')\n    else:\n        stdout.write('-1')\ndef __starting_point():\n    main()\n\ndef main():\n    def foo(x):\n        n= x\n        tsum = 0\n        while n:\n            tsum += n%10 \n            n//=10\n        return x*x + tsum*x - int(1e18)\n        \n    import matplotlib.pyplot as plt\n    y = [foo(x) for x in range(1,int(1e18)+1)]\n    x = range(1,int(1e18)+1)\n    print(y[:100])\n    plt.plot(y,x)\n    plt.show()\ndef __starting_point():\n    main()\n"
"\ndef main():\n    from sys import stdin,stdout\n    import collections\n    for _ in range(int(stdin.readline())):\n        c = collections.Counter(list(map(int,stdin.readline().split())))\n        flag = True\n        for i in c:\n            if c[i]&1:\n                flag=False\n        if flag:\n            stdout.write('YES\n')\n        else:\n            stdout.write('NO\n')\ndef __starting_point():\n    main()\n"
"\ndef main():\n    from sys import stdin,stdout\n    import bisect\n    for _ in range(int(stdin.readline())):\n        N = int(stdin.readline())\n        mat = []\n        for i in range(N):\n            mat.append(sorted(map(int,stdin.readline().split())))\n##        print(mat)\n        temp = mat[-1][-1]\n        tsum = mat[-1][-1]\n        flag = True\n        for i in range(N-2,-1,-1):\n            ind = bisect.bisect_left(mat[i],temp)-1\n            if ind == -1:\n                flag = False\n                break\n            else:\n                tsum+=mat[i][ind]\n        if flag:\n            stdout.write(str(tsum)+'\n')\n        else:\n            stdout.write('-1\n')\ndef __starting_point():\n    main()\n"


def main():

    def rev(x):
        tsum = 0
        while x:
            tsum += x % 10
            x //= 10
        return tsum
    from sys import stdin, stdout
    from math import sqrt, ceil
    n = int(stdin.readline())
    for i in range(91):
        r = i * i + (n << 2)
        x = ceil(sqrt(r))
        if x * x == r:
            num = (x - i) / 2
            if num == int(num):
                if rev(num) == i:
                    stdout.write(str(int(num)))
                    return
    stdout.write('-1')


def __starting_point():
    main()


__starting_point()
