K = int(input())
S = input()
s_num = len(S)
if K >= s_num:
    print(S)
else:
    print(S[:K] + '...')
