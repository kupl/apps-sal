s = input()
k = int(input())
n = len(s)
dic = {}
ansl = []
for i in range(n):
    for j in range(i, n):
        length = j - i + 1
        if length > k:
            continue
        partial = s[i:j + 1]
        if not dic.get(partial, False):
            dic[partial] = True
            ansl.append(partial)
ansl.sort()
print(ansl[k - 1])
