n, h = map(int, input().split())
list_AB = [ list(map(int,input().split(" "))) for _ in range(n)]
cnt = 0
A = 0

for a, b in list_AB:
    A = max(A, a)

list_AB.sort(key=lambda x:x[1], reverse=True)
for a, b in list_AB:
    if b > A:
        h -= b
        cnt += 1

    if h <= 0:
        break

if h > 0:
    if h % A == 0:
        cnt += h // A
    else:
        cnt += h // A + 1

print(cnt)
