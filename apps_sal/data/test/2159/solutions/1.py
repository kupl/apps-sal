n = int(input())
s = [int(i) for i in input().split()]

answer = [0 for i in range(n)]
p = n
for j in range(n):
    a = [0] * p
    domin = s[0]
    answer[domin - 1] += 1
    a[domin - 1] += 1
    for i in range(1, n):
        a[s[i] - 1] += 1
        if a[s[i] - 1] > a[domin - 1] or (a[s[i] - 1] == a[domin - 1] and s[i] < domin):
            domin = s[i]
        answer[domin - 1] += 1
    s.pop(0)
    n -= 1
print(*answer)
