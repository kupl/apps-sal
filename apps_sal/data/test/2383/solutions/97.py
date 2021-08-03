n = int(input())
A = list(map(int, input().split()))
prev = -1
cnt = [0]
i = 0
for a in A:
    if prev == -1 and a == 1:
        prev = a
    elif a == prev + 1:
        prev = a
    else:
        i += 1
if prev == -1:
    print(-1)
else:
    print(i)
