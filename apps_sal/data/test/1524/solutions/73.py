"""
Created on Thu Sep 10 11:58:51 2020

@author: liang
"""
S = input()
r_index = -1
l_index = -1
r_count = 0
l_count = 0
ans = [0] * len(S)
for i in range(len(S)):
    if S[i] == 'R':
        if l_index != -1:
            ans[r_index] = (r_count + 1) // 2 + l_count // 2
            ans[l_index] = (l_count + 1) // 2 + r_count // 2
            l_index = -1
            r_count = 0
            l_count = 0
        r_index = i
        r_count += 1
    else:
        if l_index == -1:
            l_index = i
        l_count += 1
ans[r_index] = (r_count + 1) // 2 + l_count // 2
ans[l_index] = (l_count + 1) // 2 + r_count // 2
print(' '.join([str(i) for i in ans]))
