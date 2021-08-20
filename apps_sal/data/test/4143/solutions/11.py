import math
N = int(input())
move = []
for i in range(5):
    move.append(int(input()))
movemin = min(move)
if movemin >= N:
    ans = 5
else:
    ans = math.ceil(N / movemin) + 4
print(ans)
