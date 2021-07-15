def main():
    from heapq import heapify, heappop
    
    n, m = [int(i) for i in input().split()]
    energy = [[int(v), i] for i, v in enumerate(input().split())]
    s_energy = sorted(energy)
    graph = [set() for i in range(n)]
    for i in range(m):
        x, y = [int(i) for i in input().split()]
        graph[x - 1].add(y - 1)
        graph[y - 1].add(x - 1)
    
    result = 0
    for i in range(n):
        e, x = s_energy.pop()
        for j in graph[x]:
            graph[j].remove(x)
            result += energy[j][0]
            
    print(result)
            

main()

