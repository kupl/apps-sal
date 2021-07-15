# n = int(input())
# ab = []
# for i in range(n):
#     ab.append(list(map(int, input().split())))

# 1 -1
# -1 -1
# -1 -1
# -1 4
# -1 -1
# -1 6

# 1 -1 1
# 2 -1 2
# -1 2 2
# -1 1 3

# people = x, floor = 2x
# 1 0
# 2 0
# 3 0 0 3
# 0 1
# 0 2
# 0 3

N = int(input())

# decided pairs
kettei = []
# all floors not decided pairs
nobori = []
kudari = []

# floors people get out
all_ori = set()
# floors people get in
all_nobori = set()

flag = False

for i in range(N):
    a, b = list(map(int, input().split()))
    if a == -1 and b == -1:
        continue
    elif a == -1:
        # never get out at first
        # never two men get out at same floor
        if b == 1 or b in all_ori:
            flag = True
        kudari.append(b)
        all_ori.add(b)
    elif b == -1:
        # never get out at top
        # never two men get in at same floor
        if a == 2 * N or a in all_nobori:
            flag = True
        nobori.append(a)
        all_nobori.add(a)
    else:
        if a >= b:
            flag = True
        else:
            if a in all_nobori or b in all_ori:
                flag = True
            kettei.append((a, b))
            all_nobori.add(a)
            all_ori.add(b)

if flag:
    print("No")
    return

dp = [-1] * (2 * N + 1)
# 1 2
# 3 4
# 5 6
# decide C from decided pairs for each floor.
# if this is mistaken, it is unfair.
for a, b in kettei:
    for i in range(a, b):
        if dp[i] == -1:
            dp[i] = b - a
        elif dp[i] != b - a:
            print("No")
            return

nobori.sort()
kudari = sorted(kudari)[::-1]

for a in nobori:
    # no problem
    if dp[a] == -1:
        continue
    else:
        # find b from decided C
        b = a + dp[a]
        # if C is not valid, it's failed
        if b > 2 * N or b in all_ori:
            print("No")
            return
        else:
            all_ori.add(b)
            for i in range(a, b):
                if dp[i] == -1:
                    dp[i] = b - a
                elif dp[i] != b - a:
                    print("No")
                    return

for b in kudari:
    if dp[b] == -1:
        continue
    else:
        a = b - dp[b]
        if a < 1 or a in all_nobori:
            print("No")
            return
        else:
            all_nobori.add(a)
            for i in range(a, b):
                if dp[i] == -1:
                    dp[i] = b - a
                elif dp[i] != b - a:
                    print("No")
                    return

print("Yes")

