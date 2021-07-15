n = int(input())
isp = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    isp.append([i+1, s, p])
isp = sorted(isp, key=lambda x: (x[1], -x[2]))
for i in isp:
    print(i[0])
