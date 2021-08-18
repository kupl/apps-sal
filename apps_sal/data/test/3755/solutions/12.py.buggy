
"""
Writer: SPD_9X2
https://atcoder.jp/contests/arc092/tasks/arc092_c

寄与を残せる要素ってどんな集合？

→少なくとも連続する2つは絶対残せない
→残せるのは、偶数番目 or 奇数番目　のみ？

→少なくとも、偶奇が違う二つの要素を同時に残す方法は見当たらない

構築→右端から構築していくのが楽？(indexが変化しないので)
後ろから見ていって、取らないと決めたindと、取ると決めたやつ+1を選んでいけばよい

全て負の時はコーナーケース
"""

import sys
N = int(input())

a = list(map(int, input().split()))

esum = 0
osum = 0

if max(a) < 0:
    # コーナーケース

    maxind = 0
    for i in range(N):
        if a[maxind] < a[i]:
            maxind = i

    rem = N
    print((a[maxind]))
    print((N - 1))
    for i in range(maxind):
        print((1))
        rem -= 1
    while rem != 1:
        print(rem)
        rem -= 1
    return

eve = 0
eflag = [False] * N
epicks = []
odd = 0
oflag = [False] * N
opicks = []
for i in range(N):

    if i % 2 == 0 and a[i] >= 0:
        eflag[i] = True
        eve += a[i]
        epicks.append(i)
    if i % 2 == 1 and a[i] >= 0:
        oflag[i] = True
        odd += a[i]
        opicks.append(i)

if eve > odd:

    print(eve)
    ans = []

    for i in range(N - 1, -1, -1):

        if i < epicks[0]:
            ans.append(1)
        elif i % 2 == 0 and eflag[i] == False:
            ans.append(i + 1)
        elif i % 2 == 1 and eflag[i - 1] == True:
            ans.append(i + 1)

    print((len(ans)))
    print(("\n".join(map(str, ans))))

else:

    print(odd)
    ans = []

    for i in range(N - 1, -1, -1):

        if i < opicks[0]:
            ans.append(1)
        elif i % 2 == 1 and oflag[i] == False:
            ans.append(i + 1)
        elif i % 2 == 0 and oflag[i - 1] == True:
            ans.append(i + 1)

    print((len(ans)))
    print(("\n".join(map(str, ans))))
