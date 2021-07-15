import sys

def main():
    n,m = map(int,sys.stdin.readline().split())

    l = [[] for i in range(n+1)]
    u = [False]*(n+1)

    for i in range(m):
        a, b = map(int,sys.stdin.readline().split())
        l[a].append(b)
        l[b].append(a)
        
    for i in range(n):
        j = i+1
        if u[j]:
            continue
        u[j] = True        
        q = []
        cl = len(l[j])
        cn = 1
        for a in l[j]:
            q.append(a)

        while len(q)!=0 :
            cur = q.pop()
            if u[cur]:
                continue
            u[cur] = True
            cn+=1
            cl+=len(l[cur])
            for a in l[cur]:
                if u[a]:
                    continue
                q.append(a)
        if cl!=cn*(cn-1):
            #print(j, cl, cn)
            print("NO")
            return
    print("YES")


main()
