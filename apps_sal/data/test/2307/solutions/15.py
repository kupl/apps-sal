T = eval(input())
t = list(map(int, input().strip().split()))
c = 0
for i in t:
    if i % 2 == 0:
        c = c + 1

if c > len(t) - c:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
