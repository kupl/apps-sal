n = int(input())
w = [input() for _ in range(n)]
# 同じ文字列が含まれていない
if len(set(w)) != n:
    print('No')
    return
# 末尾と先頭の文字が同じ（しりとり）
for i in range(1, n):
    if w[i - 1][-1] != w[i][0]:
        print('No')
        return
print('Yes')
