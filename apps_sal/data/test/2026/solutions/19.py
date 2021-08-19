n = int(input())
A = input()
count = 0
B = {'L': 0, 'R': 1, 'U': 2, 'D': 3}
C = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}
res = [0, 0, 0, 0]
for i in A:
    if res[B[C[i]]] == 0:
        res[B[i]] += 1
    else:
        count += 1
        res = [0, 0, 0, 0]
        res[B[i]] += 1
if res != [0, 0, 0, 0]:
    count += 1
print(count)
