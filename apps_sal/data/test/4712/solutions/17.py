h,w = map(int,input().split())
s = []
s.append("#"*(w+2))
for i in range(h):
    t = input()
    t = "#" + t + "#"
    s.append(t)
s.append("#"*(w+2))
for ss in s:
    print("".join(ss))
