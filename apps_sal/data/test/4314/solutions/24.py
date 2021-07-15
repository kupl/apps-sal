H,W = map(int,input().split())
ans = []
for i in range(H):
    a = input()
    if a != "."*W:
        ans.append(a)
H = len(ans)
ans2 = list(map(list,zip(*ans)))
while ["."]*H in ans2:
    ans2.remove(["."]*H)
trueans = list(map(list,zip(*ans2)))
for i in trueans:
    print("".join(i))
