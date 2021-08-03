X, Y, A, B, C = map(int, input().split())
plist = list(map(int, input().split()))
qlist = list(map(int, input().split()))
rlist = list(map(int, input().split()))

plist.sort()
qlist.sort()
rlist.sort()

plist = plist[::-1][:X]
qlist = qlist[::-1][:Y]
rlist = rlist[::-1]

pqrlist = plist + qlist + rlist
pqrlist.sort()
pqrlist = pqrlist[::-1]

print(sum(pqrlist[:X + Y]))
