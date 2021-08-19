N = int(input())
Alist = []
Blist = []
for _ in range(N):
    (a, b) = map(int, input().split())
    Alist.append(a)
    Blist.append(b)
Alist.sort()
Blist.sort()
if N % 2 == 1:
    center_A = Alist[(N - 1) // 2]
    center_B = Blist[(N - 1) // 2]
    print(int(center_B - center_A + 1))
else:
    center_A = (Alist[N // 2 - 1] + Alist[N // 2]) / 2
    center_B = (Blist[N // 2 - 1] + Blist[N // 2]) / 2
    print(int(center_B * 2 - center_A * 2 + 1))
