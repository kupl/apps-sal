(N, M) = list(map(int, input().split()))
one = []
two = []
three = []
for i in range(M):
    (s, c) = list(map(int, input().split()))
    if s == 1:
        one.append(c)
    elif s == 2:
        two.append(c)
    elif s == 3:
        three.append(c)
one = list(set(one))
two = list(set(two))
three = list(set(three))
if len(one) >= 2 or len(two) >= 2 or len(three) >= 2:
    print(-1)
elif N == 3:
    if len(one) == 0:
        one.append(1)
    else:
        one.append(0)
    if one[0] == 0:
        print(-1)
    else:
        two.append(0)
        three.append(0)
        print(one[0] * 100 + two[0] * 10 + three[0])
elif N == 2:
    if len(one) == 0:
        one.append(1)
    else:
        one.append(0)
    if one[0] == 0:
        print(-1)
    else:
        two.append(0)
        print(one[0] * 10 + two[0])
elif N == 1:
    if len(one) != 0:
        print(one[0])
    else:
        print(0)
