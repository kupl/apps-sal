3
N = int(input())
K = list(map(int, input().split()))
su = 0
for k in K:
    k -= 1
    su += k
    print(2 if su % 2 == 0 else 1)
