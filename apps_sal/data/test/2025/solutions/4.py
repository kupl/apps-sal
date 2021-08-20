n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
ans = []
for i in range(n):
    q = arr[i]
    if q % 2 == 0 and q >= 4:
        ans.append(q // 4)
    elif q % 2 == 1 and (q >= 13 or q == 9):
        ans.append(1 + (q - 9) // 4)
    else:
        ans.append(-1)
for i in range(n):
    print(ans[i])
