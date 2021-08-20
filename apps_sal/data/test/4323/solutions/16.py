(cnt, memory) = list(map(int, input().split()))
deltas = [0] * cnt
musics = []
curr_memory = 0
for ind in range(cnt):
    (full, small) = list(map(int, input().split()))
    musics.append([full, small])
    curr_memory += full
    deltas[ind] = full - small
deltas.sort()
count_changes = 0
steps = 0
while curr_memory > memory and steps < cnt:
    curr_memory -= deltas[cnt - steps - 1]
    steps += 1
if curr_memory <= memory:
    print(steps)
else:
    print(-1)
