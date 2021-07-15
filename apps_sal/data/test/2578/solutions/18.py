from sys import stdin

def find(Set, x):
    while Set[x] != x:
        Set[x] = Set[Set[x]]
        x = Set[x]

    return x 

def union(Set, u, v):
    f_u = find(Set, u)
    f_v = find(Set, v)
    
    if f_u != f_v:
        Set[f_u] = f_v

def solve():
    #stdin = open("C. News Distribution.txt")
    
    N, M = map(int, stdin.readline().split())
    
    Set = list(range(N+1))
    
    for _ in range(M):
        group = [int(k) for k in stdin.readline().split()][1:]
        
        for x in group[1:]:
            Set[find(Set, x)] = find(Set, group[0])

    cnt = [0]*(N+1)
    
    for i in range(1, N+1):
        cnt[find(Set, i)] += 1
                
    print (' '.join(map(str, [cnt[find(Set, i)] for i in range(1,N+1)])))

def __starting_point():  
    solve()
__starting_point()
