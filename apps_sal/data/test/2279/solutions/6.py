import operator

n = int(input())
dict = {}
for i in range(2, 2 * n + 1):
    L = list(map(int, input().split()))
    for j in range(len(L)):
        dict[L[j]] = (i, j + 1)

sorted_dict = sorted(dict.items(), key = operator.itemgetter(0), reverse = True)
#print(sorted_dict)
ans = [0] * 2 * n

for i in sorted_dict:
    if ans[i[1][0] - 1] == 0 and ans[i[1][1] - 1] == 0:
        ans[i[1][0] - 1] = i[1][1]
        ans[i[1][1] - 1] = i[1][0]
        
print(' '.join(map(str, ans)))
