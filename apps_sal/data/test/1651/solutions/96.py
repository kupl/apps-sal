s, p = list(map(int, input().split()))
fl = 0
for i in range(1, 1000050):
    if i * (s - i) == p:
        print("Yes")
        fl = 1
        break
if not fl:
    print("No")
