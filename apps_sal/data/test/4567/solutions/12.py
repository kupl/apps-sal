N = int(input())
s = [int(input()) for _ in range(N)]

s = sorted(s)
SUM = sum(s)

if SUM % 10 != 0:
    print(SUM)
    return

for i in range(N):
    if s[i] % 10 != 0:
        print(SUM - s[i])
        return

print(0)
