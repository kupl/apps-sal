N = int(input())
(ten, notten) = ([], [])
for i in range(N):
    s = int(input())
    ten.append(s) if s % 10 == 0 else notten.append(s)
score = sum(notten)
while score % 10 == 0:
    if len(notten) == 0:
        break
    score -= min(notten)
    notten.remove(min(notten))
if score == 0:
    print(0)
else:
    print(score + sum(ten))
