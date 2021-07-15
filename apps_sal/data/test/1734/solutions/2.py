indexs = []
for length in range(1, 10):
    for start in range(0, 9 - length + 1):
        indexs.append([start, start + length])
n = int(input())
used = {}
s = []
for i in range(n):
    s.append(input())
    for un in set(s[-1][index[0]: index[1]] for index in indexs):
        used[un] = used.get(un, 0) + 1
for num in s:
    for index in indexs:
        if used[num[index[0]: index[1]]] == 1:
            print(num[index[0]: index[1]])
            break
