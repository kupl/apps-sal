S = input()
 
# S_0 = S_1 かつ S_2 = S_3
# S_0 = S_2 かつ S_1 = S_3
# S_0 = S_3 かつ S_1 = S_2
# S_0 = S_1 = S_2 = S_3 を除外
 
if (S[0] == S[1] and S[2] == S[3] and S[1] != S[2]) or (S[0] == S[2] and S[1] == S[3] and S[0] != S[1]) or (S[0] == S[3] and S[1] == S[2] and S[0] != S[1]): print('Yes')
else: print('No')
