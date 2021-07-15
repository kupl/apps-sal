
def Solution(G):
    unvisited = { i for i in range(len(G)) }
    sol = []
    while unvisited:
        l = len(unvisited)
        a = next(iter(unvisited))
        unvisited.discard(a)
        stack = [a]
        while stack:
            v = stack.pop()
            s = unvisited & G[v]
            stack.extend(unvisited - s)
            unvisited = s
        sol.append(l - len(unvisited))
    
    sol.sort()
    print(len(sol))
    print(" ".join(map("{0}".format,sol)))

    pass
def main():
    s = input().split(" ")
    n = int(s[0])
    m = int(s[1])
    
    G=[  {i} for i in range(n) ]
    for _ in range(m):                  
        s =input().split(" ")
        n1 = int(s[0])-1
        n2 = int(s[1])-1
        G[n2].add(n1)
        G[n1].add(n2)

    Solution(G)                 


main()
