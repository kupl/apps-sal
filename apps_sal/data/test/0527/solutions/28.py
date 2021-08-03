"""
Tの文字にたいして、Sのインデックスをリストで持たせる
Tの頭から順繰りにたし上げていく（Loop数を数えること）
自分よりも大きい要素があれば、それを使うし、
なければ最も小さい要素を使いつつ、Loop数をCountUp
bisect_left()かな？

0123456
contest

01234567
sentence

s=[5]   -> 5  (6moji)
e=[4]   -> 7*1+4 (12moji)
n=[2]   -> 7*2+2 = 16
t=[3,6] -> 7*2+3 = 17
e=[4]   -> 7*2+4 = 18
n=[2]   -> 7*3+2 = 23
c=[0]   -> 7*4+0 = 28
e=[4]   -> 7*4+4 = 32 ( 33moji)
"""

from bisect import bisect_right, bisect_left
S = input()
T = input()


def calc(ch):
    return ord(ch) - ord('a')


# Tに含まれる文字に対し、Sのインデックスをふる
LST = [[] for _ in range(26)]
for t in T:
    nt = calc(t)
    if len(LST[nt]) > 0:
        continue
    for i in range(len(S)):
        if t == S[i]:
            LST[nt].append(i)
    if len(LST[nt]) == 0:
        print(-1)
        return

NS = len(S)
# Tの文字に対して順繰りにたしあげる
NofLoop = 0
now = 0
for i in range(len(T)):
    t = T[i]
    nt = calc(t)
    rel_now = now - NofLoop * NS
    if rel_now < LST[nt][0]:
        # print("R",t,nt,rel_now)
        now = NofLoop * NS + LST[nt][0] + 1
    elif LST[nt][-1] < rel_now:
        # print(t,i)
        NofLoop += 1
        now = NofLoop * NS + LST[nt][0] + 1
    else:
        idx = bisect_left(LST[nt], rel_now)
        # print(idx)
        now = NofLoop * NS + LST[nt][idx] + 1

print(now)
