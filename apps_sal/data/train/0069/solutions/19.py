"""T=int(input())
for _ in range(0,T):
    n=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""


T = int(input())
for _ in range(0, T):
    a, b = list(map(int, input().split()))
    s = input()
    ptr1 = len(s)
    ptr2 = 0
    for i in range(0, len(s)):
        if(s[i] == '1' and ptr1 == len(s)):
            ptr1 = i
        if(s[i] == '1'):
            ptr2 = i + 1

    if(ptr1 == len(s)):
        print(0)
    else:
        L1 = []
        L0 = []
        c = 1
        for i in range(ptr1 + 1, ptr2):
            if(s[i] == s[i - 1]):
                c += 1
            else:
                if(s[i - 1] == '0'):
                    L0.append(c)
                    c = 1
                else:
                    L1.append(c)
                    c = 1
        L1.append(c)

        if(len(L1) == 1):
            print(a)
        else:
            ans = a
            for i in range(0, len(L1) - 1):
                if((b * L0[i]) <= a):
                    ans += (b * L0[i])
                else:
                    ans += a
            print(ans)
