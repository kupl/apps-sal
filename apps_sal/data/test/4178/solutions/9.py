N = int(input())
H = [int(i) for i in input().split()]

s = H[0]
t = 0
for i in range(1, N):
    if s <= H[i]:
        s = max(s, H[i] - 1)
    else:
        t = 1
        break

if t == 0:
    print('Yes')
else:
    print('No')
