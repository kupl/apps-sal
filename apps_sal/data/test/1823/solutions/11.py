n, k = list(map(int, input().split()))
lis = list(map(int, input().split()))
ans = []
freq = [0] * (k + 1)
for i in range(n - 1):
    if lis[i] != lis[i + 1]:
        ans.append(lis[i])
if lis[-1] != ans[-1]:
    ans.append(lis[-1])
# print(ans,freq)
l = len(ans)
for i in range(1, l - 1):
    if ans[i - 1] == ans[i + 1]:
        freq[ans[i]] += 2
    else:
        freq[ans[i]] += 1
freq[ans[-1]] += 1
freq[ans[0]] += 1
print(freq.index(max(freq)))
