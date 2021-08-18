n = int(input())
w = [input() for i in range(n)]
m = w[0][-1]
for i in range(1, n):
    if w.count(w[i]) == 1 and m == w[i][0]:
        m = w[i][-1]
    else:
        print('No')
        return
print('Yes')
