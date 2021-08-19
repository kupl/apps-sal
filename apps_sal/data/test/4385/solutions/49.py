import itertools
a = []
for i in range(5):
    a.append(int(input()))
k = int(input())
cnt = 0
l = list(itertools.combinations(a, 2))
for i in range(len(l)):
    if abs(l[i][0] - l[i][1]) > k:
        cnt += 1
if cnt >= 1:
    print(':(')
else:
    print('Yay!')
