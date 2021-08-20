(B1, Q, L, M) = list(map(int, input().split()))
As = set(map(int, input().split()))
Bs = []
tmp = B1
cnt = 0
while abs(tmp) <= L and cnt < 100:
    if tmp not in As:
        Bs.append(tmp)
    tmp *= Q
    cnt += 1
if 32 < len(Bs):
    print('inf')
else:
    print(len(Bs))
