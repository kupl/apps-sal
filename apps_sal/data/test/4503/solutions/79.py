H, N = map(int, input().split())
for Ai in list(map(int, input().split())):
    H -= Ai
if H > 0:
    print('No')
else:
    print('Yes')
