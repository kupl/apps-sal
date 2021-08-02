N = int(input())
K = int(input())
# for i in range(100):
# for j in range(100):
#  for k in range(100):
#   if(i!=j and i!=k and j!=k):
#    if(i*(10**))
ans = 0
if(K == 3):
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                ap = 0
                bp = 0
                cp = 0
                while(a * (10**ap) <= N):  # aについてみる
                    ap += 1
                ap -= 1
                while(a * (10**ap) + b * (10**bp) <= N and bp < ap):  # bについてみる
                    bp += 1
                bp -= 1
                while(a * (10**ap) + b * (10**bp) + c * (10**cp) <= N and cp < bp):  # cについてみる
                    cp += 1
                cp -= 1
                ans += 1 + cp + (bp * (bp - 1)) // 2 + (ap * (ap - 1) * (ap - 2)) // 6
    print(ans)
elif(K == 2):
    ans = 0
    for i in range(100):
        for j in range(100):
            if(i > j):
                for a in range(1, 10):
                    for b in range(1, 10):
                        if(a * (10**i) + b * (10**j) <= N):
                            ans += 1
    print(ans)
else:
    ans = 0
    for i in range(100):
        for a in range(1, 10):
            if(a * (10**i) <= N):
                ans += 1
    print(ans)
