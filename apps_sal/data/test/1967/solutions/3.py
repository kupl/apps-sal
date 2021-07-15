w, h = map(int, input().split())
file = [[] for i in range(w)]

for i in range(h):
    l  = list(input())
    for j in range(w):
        file[j].append(l[j])

for i in range(w):
    print(''.join([c*2 for c in file[i]]))
    print(''.join([c*2 for c in file[i]]))
