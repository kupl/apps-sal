n, m, k = list(map(int, input().split()))
a = [0] * 99
for i in range(n):
    s = input()
    for j in range(m):
        a[j] += s[j] == 'Y'
print(len(list([x for x in a if x >= k])))
#kitten

