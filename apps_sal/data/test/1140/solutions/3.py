n = int(input())
flowers = list(map(int, input().split()))
flowers.sort()
mx = 0
cl = 1
while cl < n and flowers[cl] == flowers[0]:
    cl += 1
cr = 1
while -1 - cr >= -n and flowers[-1 - cr] == flowers[-1]:
    cr += 1
if flowers[-1] != flowers[0]:
    print(flowers[-1] - flowers[0], cl * cr)
else:
    print(0, n * (n - 1) // 2)
