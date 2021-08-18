N = int(input())
SP = [list(input().split()) for _ in range(N)]

for i in range(N):
    SP[i].append(i + 1)

ans = sorted(SP, key=lambda x: (x[0], -int(x[1])))


for i in ans:
    print(i[2])
