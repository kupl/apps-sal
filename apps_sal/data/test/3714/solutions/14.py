def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return int(a * b / gcd(a, b))
    
def run(n, crush):
    visited = [False] * n
    cycle_size = 1
    
    for i in range(0, n):
        if visited[i]:
            continue
        x = i
        c = 0
        while (not visited[x]):
            visited[x] = True
            x = crush[x] - 1
            c += 1
        if x != i:
            return -1
            
        if c % 2 == 0:
            c /= 2
        cycle_size = lcm(cycle_size, c)
    
    return cycle_size
    
n = int(input())
crush = [int(x) for x in input().split()]
print(run(n,crush))

