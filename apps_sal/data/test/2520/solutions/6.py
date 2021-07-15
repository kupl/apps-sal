import sys,collections
input = sys.stdin.readline

def main():
    N,M,K = list(map(int,input().split()))
    fr = [[] for i in range(N+1)]
    bl = [[] for i in range(N+1)]

          
    for _ in range(M):
        a,b = list(map(int,input().split()))
        fr[a].append(b)
        fr[b].append(a)
    for _ in range(K):
        c,d = list(map(int,input().split()))
        bl[c].append(d)
        bl[d].append(c)

    fl = [-1 for i in range(N+1)]
    fl[0] = 0
    fl[1] = 1
    nxt = 1
    dic = {}
    s = set(range(1,N+1))
    while nxt != 0:
        q = collections.deque([nxt])
        
        fl[nxt]=nxt
        cnt = 0
        while q:
            now = q.popleft()
            s.discard(now)
            for f in fr[now]:
                if fl[f] == -1:
                    fl[f] = nxt
                    cnt +=1
                    q.append(f)
        dic[nxt] = cnt
        #try:
            #nxt = fl.index(-1)
        #except:
            #nxt = 0
        if len(s) == 0:
            nxt = 0
        else:
            nxt = s.pop()


    mbf = collections.deque()
    for i in range(1,N+1):
        ff = 0
        for j in bl[i]:
            if fl[j] == fl[i]:
                ff -= 1
        
        ff += dic[fl[i]]-len(fr[i])
        mbf.append(ff)
    print((*mbf))

def __starting_point():
    main()

__starting_point()
