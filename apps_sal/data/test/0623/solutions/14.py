def find(n1, n2):
    if n1 < 0 or n2 < 0:
        return -1
    if n1 == 0 or n2 == 0:
        return 0
    if res[n1][n2] != -1:
        return res[n1][n2]
    else:
        rel = max(find(n1 + 1, n2 - 2), find(n1 - 2, n2 + 1)) + 1
        res[n1][n2] = rel
        return rel


(n1, n2) = map(int, input().split())
res = [[-1] * 301 for i in range(301)]
print(find(n1, n2))
