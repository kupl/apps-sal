"""
Created on Tue Sep  8 01:23:04 2020

@author: liang
"""

N = int(input())
S = input()
R_list = list()
G_list = list()
B_list = list()

for i in range(N):
    if S[i] == 'R':
        R_list.append(i)
    elif S[i] == 'G':
        G_list.append(i)
    else:
        B_list.append(i)
ans = len(R_list) * len(G_list) * len(B_list)
"""
set1 = set()
for r in R_list:
    for g in G_list:
        if r > g:
            r, g = g, r 
           
            【rは絶対書き換えたらダメ】
            gのfor文中 rの値は固定して考えているので、
            外側ループの変数を書き換えるような演算をしてはいけない
              => for文内で別の変数（コピー）を用意し、そのコピーについて演算を行うこと
           
        if 2*g - r < N and S[2*g-r] == 'B':
            set1.add((r,g))
            ans -= 1
        if 2*r - g >= 0 and S[2*r-g] == 'B':
            set1.add((r,g))
            ans -= 1
        if (r+g)%2 == 0 and S[(r+g)//2] =='B':
            set1.add((r,g))
            ans -= 1   
"""
for r in R_list:
    for g in G_list:
        up = max(r, g)
        down = min(r, g)
        diff = up - down
        if up + diff < N and S[up + diff] == 'B':
            ans -= 1
        if down - diff >= 0 and S[down - diff] == 'B':
            ans -= 1
        if diff % 2 == 0 and S[down + diff // 2] == 'B':
            ans -= 1

print(ans)
