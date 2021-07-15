from sys import stdin

def getval():
    n,m,k = map(int,stdin.readline().split())
    a = [list(map(int,stdin.readline().split())) for i in range(m)]
    c = [list(map(int,stdin.readline().split())) for i in range(k)]
    return n,m,k,a,c 

def main(n,m,k,a,c):
    #Compute all members' friends
    friends = [[] for i in range(n)]
    for i in a:
        friends[i[0]-1].append(i[1]-1)
        friends[i[1]-1].append(i[0]-1)
    
    #Group all members in the isolated "friend groups"
    frgroups = []
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i]:
            continue
        q = [i]
        temp = [i]
        visited[i] = True
        while q:
            idx = q.pop(0)
            adj = friends[idx]
            for j in adj:
                if visited[j]:
                    continue
                visited[j] = True
                q.append(j)
                temp.append(j)
        frgroups.append(temp)    

    #Number all members with their friend groups respectively
    groups = [-1 for i in range(n)]
    for i in range(len(frgroups)):
        for j in frgroups[i]:
            groups[j] = i 
            
    #For each member, refer to the friend groups of blocked peope
    #Compute ans accordingly
    ans = [len(frgroups[groups[i]])-1-len(friends[i]) for i in range(n)]
    for i in c:
        if groups[i[0]-1]==groups[i[1]-1]:
            ans[i[0]-1] -= 1
            ans[i[1]-1] -= 1
    s = str(ans[0])
    for i in range(1,n):
        s += " " + str(ans[i])
    print(s)
    

def __starting_point():
    n,m,k,a,c = getval()
    main(n,m,k,a,c)
__starting_point()
