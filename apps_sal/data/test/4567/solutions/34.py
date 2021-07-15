N = int(input())
S = []
for _ in range(N):
    S.append(int(input()))

s = sum(S)
if s % 10 != 0:
    print(s)
else:
    S.sort()
    for i in S:
        if i % 10 != 0:
            s -= i
            break
    if s % 10 == 0:
        print(0)
    else:
        print(s)
