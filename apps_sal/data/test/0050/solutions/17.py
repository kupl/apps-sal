(N, M, R) = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
if b[0] < c[-1]:
    cnt = R // b[0]
    R %= b[0]
    R += cnt * c[-1]
print(R)
