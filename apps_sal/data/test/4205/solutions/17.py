N = int(input())
P = list(map(int, input().split()))

sp = sorted(P)
cnt = 0
for a, b in zip(sp, P):
    if a != b:
        cnt += 1
if cnt == 2 or cnt == 0:
    print("YES")
else:
    print("NO")
