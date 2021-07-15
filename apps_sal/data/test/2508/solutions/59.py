from sys import stdin
def input():
    return stdin.readline().strip()

import heapq

def main():
    h, w, k = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    # surround the square with '@'
    c = [['@'] * (w+2)]
    for _ in range(h):
        i = input()
        l = ['@']
        for j in i:
            l.append(j)
        l.append('@')
        c.append(l)
    c.append(['@'] * (w+2))

    # Dijkstra
    # seen[x][y] = the minimum cost of (x, y)
    # if seen[x][y] == -1, (x, y) is unresearched
    seen = [[-1] * (w+2) for _ in range(h+2)]

    # todo[i] == (cost, x, y, direction)
    todo = [(0, x1, y1, 0)]
    heapq.heapify(todo)

    # direction
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while len(todo) > 0:
        cost, xi, yi, direction = heapq.heappop(todo)

        # only straight
        if seen[xi][yi] != -1:
            if (seen[xi][yi]+k-1)//k * k > cost:
                xj, yj = xi + dx[direction], yi + dy[direction]
                if c[xj][yj] == '.':
                    heapq.heappush(todo, (cost+1, xj, yj, direction))
            continue
        seen[xi][yi] = cost

        # goal
        if xi == x2 and yi == y2:
            print((cost+k-1)//k)
            return
        
        # 4 directions
        for j in range(4):
            xj, yj = xi + dx[j], yi + dy[j]
            if c[xj][yj] == '.':
                if j == direction:
                    if seen[xj][yj] == -1 or (seen[xj][yj]+k-1)//k * k > cost:
                        heapq.heappush(todo, (cost+1, xj, yj, j))
                elif seen[xj][yj] == -1:
                    heapq.heappush(todo, ((cost+k-1)//k * k + 1, xj, yj, j))

    print(-1)

main()
