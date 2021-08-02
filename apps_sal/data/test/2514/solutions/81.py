N = int(input())
Alist = list(map(int, input().split()))
sum1 = sum(Alist)
dic = {}
for a in Alist:
    if not a in dic:
        dic[a] = 0
    dic[a] += 1

Q = int(input())
Qlist = []
for _ in range(Q):
    Qlist.append(list(map(int, input().split())))
for q in Qlist:
    b, c = q
    n = 0
    if b in dic:
        n = dic[b]
        dic[b] = 0
    else:
        pass

    if c in dic:
        dic[c] += n
    else:
        dic[c] = n
    sum1 += n * (c - b)

    print(sum1)
