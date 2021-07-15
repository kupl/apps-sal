n = int(input())
w = [input() for _ in range(n)]

for i in range(n-1):
    if w[i][-1] != w[i+1][0]:
        print('No')
        return

if len(set(w)) != n:
    print('No')
else:
    print('Yes')
