#!/usr/local/bin/python3
n, m, k = map(int, input().split())
room = [[] for i in range(m)]
result = [0] * n
cnt = [0] * m
for i in range(n):
    for n_room, n_be in enumerate(list(input().split())):
        if n_be == '1':
            room[n_room].append(i)
for i in range(k):
    n_person, n_room = map(int, input().split())
    result[n_person - 1] -= 1
    cnt[n_room - 1] += 1
for n_room, n_cnt in enumerate(cnt):
    for i in room[n_room]:
        result[i] += n_cnt
print(' '.join(map(str, result)))
