n = int(input())
l_3 = []
l_5 = []
t3 = 1
t5 = 1
for i in range(100):
    t3 *= 3
    t5 *= 5
    l_3.append(t3)
    l_5.append(t5)
ans_3 = -1
ans_5 = -1
for i in l_3:
    for j in l_5:
        if i + j == n:
            ans_3 = i
            ans_5 = j
if ans_3 != -1:
    print(l_3.index(ans_3) + 1, l_5.index(ans_5) + 1)
else:
    print(-1)
