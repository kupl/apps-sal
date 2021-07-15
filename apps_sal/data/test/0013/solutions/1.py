import sys

def main():

    n,k = map(int,sys.stdin.readline().split())
    courses = list(map(int,sys.stdin.readline().split()))
    courses = [x-1 for x in courses] 

    visited = [False]*n
    used = [False]*n

    ans = []
    t = []

    for i in range(n):
        temp = list(map(int,sys.stdin.readline().split()))
        temp = [x-1 for x in temp] 
        t.append(temp[1:])
        
    for i in range(k):
        c = courses[i]
        if used[c]:
            continue
        
        q = [c]        
        visited[c]=True
        while len(q)>0:
            cur = q[-1]
            if len(t[cur])!=0:
                s = t[cur].pop()
                if visited[s] and not used[s]:                    
                    print(-1)
                    return
                if used[s]:
                    continue                
                q.append(s)
                visited[s]=True
            else:
                ans.append(cur)
                q.pop()
                used[cur] = True

    ans = [str(x+1) for x in ans] 
    print(len(ans))
    print(" ".join(ans))

main()
