# C - Fair Elevator
n = int(input())
c = {}  # 乗り降りする階をカウント。2個以上存在したらNoとする。
p = {}  # 乗り降りする階が確定している場合、その階のペアを格納。
s = set()  # 降りる階が-1のときの乗る階。
e = set()  # 乗る階が-1のときの降りる階。
for i in range(n):
    a, b = list(map(int, input().split()))
    if a in c:
        c[a] += 1
    else:
        c[a] = 1
    if b in c:
        c[b] += 1
    else:
        c[b] = 1
    if a > 0 and b > 0:
        if a >= b:
            print('No')
            return
        else:
            p[a] = b
    elif a > 0:
        s.add(a)
    else:
        e.add(b)

for k, v in list(c.items()):
    if k < 0:
        continue
    if v > 1:
        print('No')
        return

# dp[i]:i*2階までみて、正しいa,bの組み合わせがあるか否か。
# dp[i]がTrueのときに、dp[i+1]以降に正しいa,bの組み合わせがあるか否か検証する。
# 正しい組み合わせのとき、各階をいくつかのブロックにわけることができ、
# 同じブロックでは降りる階-乗る階が等しくなる。
dp = [False for _ in range(n + 1)]
dp[0] = True
for i in range(n):
    if not dp[i]:
        continue
    for j in range(i + 1, n + 1):
        if dp[j]:
            continue
        f = True
        for k in range(j - i):
            x = i * 2 + k + 1  # 乗る階
            y = x + (j - i)  # 降りる階
            # print(i,j,x,y)
            if x in p:
                if p[x] != y:
                    f = False
                    break
            if x in s and y in e:
                f = False
                break
            if x in e:
                f = False
                break
            if y in s:
                f = False
                break
        if f:
            dp[j] = True
print(('Yes' if dp[-1] else 'No'))
# print(dp)
