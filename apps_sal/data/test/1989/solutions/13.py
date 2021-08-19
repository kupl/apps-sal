import sys
input = sys.stdin.readline
n = int(input())
ar = list(map(int, input().split()))
li = []
dic = {}
for i in range(1, n + 1):
    if ar[-i] in dic:
        dic[ar[-i]] += 1
    else:
        dic[ar[-i]] = 1
    li.append(dic[ar[-i]])
br = [0] * (n + 1)
for i in range(n):
    br[li[i]] += 1
for idx in range(1, n + 1):
    idx2 = idx + (idx & -idx)
    if idx2 < n:
        br[idx2] += br[idx]
main = 0
front = []
dic = {}
for i in range(n):
    if ar[i] in dic:
        dic[ar[i]] += 1
    else:
        dic[ar[i]] = 1
    front.append(dic[ar[i]])
for i in range(n - 1):
    inp = li[n - i - 1]
    add = -1
    while inp < n + 1:
        br[inp] += add
        inp += inp & -inp
    if inp != 1:
        inp -= 1
        add = 1
        while inp < n + 1:
            br[inp] += add
            inp += inp & -inp
    ans = 0
    inp = front[i]
    if inp != 1:
        inp -= 1
        while inp:
            ans += br[inp]
            inp -= inp & -inp
        main += ans
print(main)
