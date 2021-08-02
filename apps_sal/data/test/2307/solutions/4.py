t = int(input())
e = 0
o = 0
a = list(map(int, input().split()))
for i in a:
    if i % 2 == 1:
        o += 1
    else:
        e += 1
if e > o:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
