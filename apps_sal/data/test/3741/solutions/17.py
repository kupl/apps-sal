from sys import maxsize as INT_MAX
from collections import deque

n = int(input())
linea = input()
sep = linea.split()
nodos = list(map(int, sep))
bits = [list() for i in range(64)]
j = 0
for s in nodos:
    if s != 0:
        for i in range(64):
            bit = (s >> i) & 1
            if bit == 1:
                bits[i].append(j)
    else:
        j -= 1
        n -= 1
    j += 1
dos = False
ejecucion = True
gr = [list() for i in range(n)]
for k in bits:
    if len(k) == 2:
        dos = True
        x = k[0]
        y = k[1]
        gr[x].append(y)
        gr[y].append(x)
    elif len(k) >= 3:
        ejecucion = False
        break
if ejecucion == False:
    print(3)
elif not dos:
    print(-1)
else:
    # Python3 implementation of the approach

    # Function to find the length of
    # the shortest cycle in the graph
    def shortest_cycle(n: int) -> int:

        # To store length of the shortest cycle
        ans = INT_MAX

        # For all vertices
        for i in range(n):

            # Make distance maximum
            dist = [int(1e9)] * n

            # Take a imaginary parent
            par = [-1] * n

            # Distance of source to source is 0
            dist[i] = 0
            q = deque()

            # Push the source element
            q.append(i)

            # Continue until queue is not empty
            while q:

                # Take the first element
                x = q[0]
                q.popleft()

                # Traverse for all it's childs
                for child in gr[x]:

                    # If it is not visited yet
                    if dist[child] == int(1e9):

                        # Increase distance by 1
                        dist[child] = 1 + dist[x]

                        # Change parent
                        par[child] = x

                        # Push into the queue
                        q.append(child)

                    # If it is already visited
                    elif par[x] != child and par[child] != x:
                        ans = min(ans, dist[x] +
                                  dist[child] + 1)

        # If graph contains no cycle
        if ans == INT_MAX:
            return -1

        # If graph contains cycle
        else:
            return ans

    # Function call
    print(shortest_cycle(n))

    # This code is contributed by
    # sanjeev2552
