def solve(n,s,closed):
    min_moves = float('inf')
    floor = s
    time = 0
    while floor > 0:
        if floor not in closed:
            min_moves = min(min_moves,time)
            break
        floor -= 1
        time += 1

    floor = s
    time = 0
    while floor <= n:
        if floor not in closed:
            min_moves = min(min_moves,time)
            break
        floor += 1
        time += 1

    print(min_moves)

def main():
    t = int(input())
    for i in range(t):
        n,s,k = list(map(int,input().split()))
        closed = set(map(int,input().split()))
        solve(n,s,closed)

    
main()

