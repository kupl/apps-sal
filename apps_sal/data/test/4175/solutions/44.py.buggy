n = int(input())
w = [input() for _ in range(n)]
if len(set(w)) != n:
    print('No')
    return
for i in range(1, n):
    if w[i - 1][-1] != w[i][0]:
        print('No')
        return
print('Yes')
