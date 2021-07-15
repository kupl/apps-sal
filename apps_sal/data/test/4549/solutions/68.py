H, W = map(int, input().split())
S = ['.' + input() + '.' for _ in range(H)]
S = ['.'*(W+2)] + S + ['.'*(W+2)]
flag = 0
for i in range(1, H+1):
    for j in range(1,W+1):
        if S[i][j] == '#':
            if S[i-1][j] == '.' and S[i+1][j] == '.' and S[i][j-1] == '.' and S[i][j+1] == '.':
                flag = 1
print('Yes' if flag == 0 else 'No')
