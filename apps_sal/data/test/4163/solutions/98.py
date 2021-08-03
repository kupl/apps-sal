N = int(input())
c = 0
d = 0
for i in range(N):
    s = list(map(int, input().split()))
    if s[0] == s[1]:
        c = c + 1
        if c == 3:
            d = d + 1
    else:
        c = 0

if d > 0:
    print("Yes")
else:
    print("No")
