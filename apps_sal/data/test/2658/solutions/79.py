N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

count = 0

stack = set()
visited = []
visited_set = set()
endf = False

current = 0
while True:
    i = A[current]-1
    visited_set.add(current)
    visited.append(current)

    if not i in visited_set:
        current = i
        count += 1
    else:
        leng = len(visited_set)
        roop_len = leng - visited.index(i)
        header_len = leng - roop_len
        break

    if count >= K:
        endf = True
        print(i+1)
        break

if not endf:
    roop_ind = (K - header_len + 1) % roop_len
    if roop_ind == 0:
        print(visited[-1]+1)
    else:
        print(visited[header_len + roop_ind-1]+1)
