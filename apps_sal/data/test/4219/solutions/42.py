N = int(input())

mastar_list = []
for i in range(2 ** N):
    x = "{:0" + str(N) + "b}"
    mastar_list.append(list(map(int, x.format(i))))


current = 1
ans = []
judge = [True for i in range(2 ** N)]
while current <= N:
    now = current - 1
    loop_num = int(input())
    for i in range(loop_num):
        a, b = list(map(int, input().split()))
        c = a - 1
        for index, situation in enumerate(mastar_list):
            if situation[now] == 1:
                if situation[c] == b:
                    pass
                else:
                    judge[index] = False
            else:
                pass
    current += 1

ans = []
for index, content in enumerate(judge):
    if content:
        ans.append(sum(mastar_list[index]))

print((max(ans)))
