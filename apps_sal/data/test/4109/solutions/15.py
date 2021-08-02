import itertools
n, m, x = map(int, input().split())
books = []
for i in range(n):
    ins = list(map(int, input().split()))
    books.append({"c": ins[0], "a": ins[1: m + 1]})
ans = float('inf')
for i in range(1, n + 1):
    book_list = list(itertools.combinations(list(range(n)), i))
    for lis in book_list:
        cost_sum = 0
        a_sum = [0] * m
        ok = 0
        ok_list = [False] * m
        for j in lis:
            cost_sum += books[j]['c']
            for k in range(m):
                a_sum[k] += books[j]['a'][k]
                if not ok_list[k] and a_sum[k] >= x:
                    ok += 1
                    ok_list[k] = True
        if ok == m and ans > cost_sum:
            ans = cost_sum
if ans == float('inf'):
    print(-1)
else:
    print(ans)
