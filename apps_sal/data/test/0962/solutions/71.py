from collections import deque
import sys

N,M = list(map(int,input().split()))

AB = []
lis = [ [] for i in range(N)]

for i in range(M):

    A,B = list(map(int,input().split()))

    A -= 1
    B -= 1

    lis[A].append(B)

q = deque([])

first = [-1] * (N+1)
first[0] = 0
first[-1] = 0

q.append( first )

end = [True] * N
end[0] = False

while len(q) > 0:

    now = q.pop()
    lasp = now[-1]
    nownum = now[lasp] 

    #print (q,now,lasp,nownum)

    for nex in lis[lasp]:

        if now[nex] == -1:
            ncopy = now.copy()
            ncopy[nex] = nownum + 1
            ncopy[-1] = nex
            end[nex] = False
            q.append(ncopy)

        else:

            flag = True

            for i in range(N):

                if now[i] >= 0:

                    for j in lis[i]:

                        if (now[j] >= now[nex] and now[j] != now[i] + 1) and not (i == lasp and j == nex):
                            flag = False
                            break

                if not flag:
                    break

            if flag:
                ans = []

                for i in range(N):
                    if now[i] >= now[nex]:
                        ans.append(i + 1)

                print((len(ans)))
                for i in ans:
                    print (i)

                return

    if len(q) == 0:
        for i in range(N):
            if end[i]:

                first = [-1] * (N+1)
                first[i] = 0
                first[-1] = i
                q.append(first)
                end[i] = False
                break
            #print (flag,nex,lasp)

print((-1))

