n, k = [int(x) for x in input().split()]

L = [int(x) for x in input().split()]

s = input()

temp = [1, 0, 0]
R = []
for i in range(n - 1):
    if s[i + 1] == s[i]:
        temp[0] += 1
    else:
        temp[-1] = i
        R.append(temp)
        temp = [1, i + 1, i + 1]

temp[-1] = n - 1
R.append(temp)
Dam = 0
for i in R:
    if i[0] > k:
        q = L[i[1]:i[2] + 1]
        q.sort(reverse=True)
        t = 0
        for i in range(k):
            t += q[i]
        Dam += t
    else:
        Dam += sum(L[i[1]:i[2] + 1])

print(Dam)
