n = int(input())
l = list(map(int,input().split()))

# 一番長い辺が他のN−1辺の長さの合計よりも真に短い場合に限り、条件を満たすN角形が描ける。
if sum(l) - max(l) > max(l):
    print("Yes")
else:
    print("No")
