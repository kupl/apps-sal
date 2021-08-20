(n, m, k) = map(int, input().split())
room = [[] for i in range(m)]
person = []
result = [0] * n
for i in range(n):
    person.append(list(input().split()))
for i in range(n):
    n_room = 0
    for n_be in person[i]:
        if n_be == '1':
            room[n_room].append(i)
        n_room += 1
cnt = [0] * m
for i in range(k):
    (n_person, n_room) = map(int, input().split())
    n_person -= 1
    n_room -= 1
    result[n_person] -= 1
    cnt[n_room] += 1
for (n_room, n_cnt) in enumerate(cnt):
    for i in room[n_room]:
        result[i] += n_cnt
print(' '.join(map(str, result)))
