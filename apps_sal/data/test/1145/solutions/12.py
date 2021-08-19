n = int(input())
arr = list(map(int, input().split()))
count = [0] * 6002
m = 1
for i in range(n):
    count[arr[i]] += 1
    m = max(m, arr[i])
ans = []
for i in range(1, 6002):
    if count[i] == 0:
        ans.append(i)
s = 0
ind = 0
for i in range(1, m + 1):
    if count[i] != 0:
        while count[i] != 1:
            if ans[ind] > i:
                s += ans[ind] - i
                count[i] -= 1
            ind += 1
print(s)
