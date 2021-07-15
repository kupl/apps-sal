N = int(input())

W = []

for i in range(N):
    W.append(input())

cnt = set()
last = W[0][-1]
for i, w in enumerate(W):
    if i == 0:
        cnt.add(w)
        continue
    if w[0] != last:
        print('No')
        return
    last = w[-1]
    cnt.add(w)
    if i+1 != len(cnt):
        print('No')
        return

print('Yes')

