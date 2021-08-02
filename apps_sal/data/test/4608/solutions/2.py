N = int(input())
l = [int(input()) - 1 for _ in range(0, N)]

i = 0;
flg = False

for n in range(0, N):
    if l[i] == 1:
        print(n + 1)
        flg = True
        break
    else:
        i = l[i]


if not flg:
    print("-1")
