a,ma = input().split()
a,ma = int(a),int(ma)
c = [int(x) for x in input().split()]
sm = 0
for x in c:
    sm += x
sm = abs(sm)
if sm/ma != int(sm/ma):
    res = int(sm/ma)+1
else:
    res = int (sm/ma)
print(res)

