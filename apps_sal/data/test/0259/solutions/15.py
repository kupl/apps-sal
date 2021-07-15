N, T = list(map(int, input().split()))
bt = -1
br = -1
for n in range(N):
    s, d = list(map(int, input().split()))
    if s >= T:
        a = s
    else:
        a = (T-s+d-1) // d
        a = s+d*a
    if bt == -1 or a < bt:
        bt = a
        br = n+1
print(br)

