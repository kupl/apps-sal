n = int(input())
arr = ['RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR']
s = input()
cnts = []
for i in arr:
    cnt = 0
    for j in range(len(s)):
        if s[j] == i[j % 3]:
            cnt += 1
    cnts.append(cnt)
k = cnts.index(max(cnts))
s = arr[k] * (n // 3 + 1)
s = s[:n]
print(n - max(cnts))
print(s)
