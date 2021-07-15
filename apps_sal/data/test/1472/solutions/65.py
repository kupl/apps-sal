N, X, Y = map(int, input().split())

distance = [[] for i in range(N-1)]
for i in range(1, N):
    for j in range(i+1, N+1):
        distance[i-1].append(min(abs(j-i), abs(X-i)+1+abs(j-Y), abs(Y-i)+1+abs(j-X)))

count = [0 for i in range(N)]
for i in range(N-1):
    for dis in distance[i]:
        count[dis] += 1
        
for i in range(1, len(count)):
    print(count[i])
