N, H = map(int, input().split())
slash = 0
Throw = []
for _ in range(N):
    a, b = map(int, input().split())
    slash = max(slash, a)
    if b > a: Throw.append(b)    
#slash=斬撃最大ダメージ、投げてslash超のダメージが出るならばその刀をダメージが大きい順に投げる
Throw = sorted([th for th in Throw if th > slash], reverse=True)
dmg, cnt = 0, 0
for throw in Throw:
    if dmg >= H: break
    dmg += throw
    cnt += 1
if dmg < H:
    from math import ceil
    cnt += ceil((H-dmg)/slash)
print(cnt)
