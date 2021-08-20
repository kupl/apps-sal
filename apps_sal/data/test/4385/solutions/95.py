t = []
for i in range(5):
    t.append(int(input()))
k = int(input())
t.sort()
if t[4] - t[0] > k:
    print(':(')
else:
    print('Yay!')
