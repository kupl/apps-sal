n, k, p = list(map(int, input().split()))
l = list(map(int, input().split()))
odd, even = [], []
for i in l:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
if (len(odd) - (k - p)) % 2 != 0:
    print("NO")
    return
ans = [[] for _ in range(k)]
for i in range(k - p):
    if odd:
        ans[i].append(odd.pop())
    else:
        print("NO")
        return
for i in range(k - p, k):
    if even:
        ans[i].append(even.pop())
    elif len(odd) >= 2:
        ans[i].append(odd.pop())
        ans[i].append(odd.pop())
    else:
        print("NO")
        return
ans[0] += even + odd
print("YES")
for i in ans:
    print(len(i), *i)
