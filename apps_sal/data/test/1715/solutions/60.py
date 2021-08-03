from bisect import bisect_left
a, b, q = list(map(int, input().split()))
INF = 10**15
s = [-INF] + sorted([int(input()) for _ in range(a)]) + [INF]
t = [-INF] + sorted([int(input()) for _ in range(b)]) + [INF]
# print(s,t)
for i in range(q):
    pro = int(input())
    s_index = bisect_left(s, pro)
    t_index = bisect_left(t, pro)
    s1, s2 = s[s_index - 1], s[s_index]
    t1, t2 = t[t_index - 1], t[t_index]
    # print(s1,s2,t1,t2)
    minimum = []
    kouho1 = abs(pro - s1) + abs(s1 - t1)
    minimum.append(kouho1)
    kouho2 = abs(pro - s1) + abs(s1 - t2)
    minimum.append(kouho2)
    kouho3 = abs(pro - t1) + abs(t1 - s1)
    minimum.append(kouho3)
    kouho4 = abs(pro - t2) + abs(t2 - s1)
    minimum.append(kouho4)
    kouho5 = abs(pro - s2) + abs(s2 - t1)
    minimum.append(kouho5)
    kouho6 = abs(pro - s2) + abs(s2 - t2)
    minimum.append(kouho6)
    kouho7 = abs(pro - t1) + abs(s2 - t1)
    minimum.append(kouho7)
    kouho8 = abs(pro - t2) + abs(s2 - t2)
    minimum.append(kouho8)
    print((min(minimum)))
