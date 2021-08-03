n, k = list(map(int, input().split()))
ins = list(map(int, input().split()))
index = list(range(n))
index.sort(key=lambda x: ins[x])
days = 0
i = 0
ans = []
while True:
    if i >= n:
        break
    days += ins[index[i]]
    if days > k:
        break
    else:
        ans.append(index[i] + 1)
    i += 1

print(i)
if i != 0:
    print(" ".join(map(str, ans)))
