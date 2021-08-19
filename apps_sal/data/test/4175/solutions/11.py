n = int(input())
arr = []
ans = 'Yes'
for _ in range(n):
    w = input()
    if w in arr:
        ans = 'No'
    if len(arr) >= 1:
        if w[0] != arr[-1][-1]:
            ans = 'No'
    arr.append(w)
print(ans)
