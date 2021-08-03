n, k = list(map(int, input().split()))
l1 = list(map(int, input().split()))
l11 = []
l_s = []
m_v = 0
for ev in l1:
    l11.append(ev)
    l_s.append(ev)
l_s.sort()
if (k == 1):
    print(int(min(l11)))
elif (k >= 3):
    print(int(max(l11)))
elif (k == 2):
    if l11[0] > l11[n - 1] and l11[0] != l_s[0]:
        print(l11[0])
    elif l11[0] < l11[n - 1] and l11[n - 1] != l_s[0]:
        print(l11[n - 1])
    else:
        print(l11[0])
