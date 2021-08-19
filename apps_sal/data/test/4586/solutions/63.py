# 4桁の数字で3つ以上連続するか判定

N = list(input())
# print(N)

if N[0] == N[1] and N[0] == N[2]:
    print('Yes')
elif N[1] == N[2] and N[1] == N[3]:
    print('Yes')
else:
    print('No')
