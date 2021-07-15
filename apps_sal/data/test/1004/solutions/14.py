N = int(input())
A = list(map(int, input().split()))
Q = []
L = [0] * (10**6+1)
Ans = []
cnt = 0
cnt_emp = 0
for a in A:
    cnt += 1
    if a>0:
        Q.append(a)
        l = L[a]
        if l==0:
            L[a] = 1
            cnt_emp += 1
        elif l==1:
            print(-1)
            return
        else:
            print(-1)
            return
    else:
        a = -a
        l = L[a]
        if l==0:
            print(-1)
            return
        elif l==1:
            L[a] = 2
            cnt_emp -= 1
            if cnt_emp==0:
                Ans.append(cnt)
                cnt = 0
                for q in Q:
                    L[q] = 0
                Q = []
        else:
            print(-1)
            return
if cnt_emp!=0:
    print(-1)
    return
print(len(Ans))
print(" ".join(map(str, Ans)))

