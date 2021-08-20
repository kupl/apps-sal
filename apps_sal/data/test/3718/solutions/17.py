def __starting_point():
    n = int(input())
    b = sorted(set(map(int, input().split(' '))))
    for i in range(len(b) - 2):
        if len(set(b[i:i + 3])) == 3:
            if b[i + 2] - b[i] <= 2 and b[i + 2] - b[i + 1] <= 1:
                print('YES')
                break
    else:
        print('NO')


"\n    A = input()\n    stack = []      #Real Stack\n    Graph = {\n        ')':'('\n        }\n    count = 0\n    def black(A):\n        #p for possibility\n        stak =[]\n        for e in A:\n            if e in ['(']:\n                stak.append(e)\n            else:\n                if stak==[] or Graph[e]!=stak[-1]:\n                    p=False\n                else:\n                    stak.pop(len(stak)-1)     #pop last \n        if len(stak) ==0:\n            p=True\n        else:\n            p=False\n        if not p:   return [0]\n        else:\n            #stak is not empty\n            stak = []\n            count = []\n            for e in range(len(A)):\n                if A[e]=='(' or stak==[]:  stak.append(A[e])\n                else:\n                    if A[e]==')' and Graph[A[e]]==stak[-1]:\n                        while Graph[A[e]]==stak[-1]:\n                            stak.pop(-1)\n                            if e==len(A)-1: break\n                            e+=1\n                            if A[e]=='(' or stak==[]:   break\n                        count.append(1)\n            return count\n\n    rov = []\n    P = False \n    for e in A:\n        if e in ['(']:  stack.append(e)\n        else:\n            if stack!=[]:\n                stack.append(e)\n                if stack.count('(')==stack.count(')'):\n                    x=black(stack)\n                    if x!=[0]:    P = True\n                    if x==[1]:\n                        rov.append(1)\n                    else:\n                        rov.append(sum(x[:-1]))\n                    stack=[]\n    if not P:   print(0)\n    else:\n        pro =1\n        for i in rov:   pro*=i\n        print(pro)\n    \n"
__starting_point()
