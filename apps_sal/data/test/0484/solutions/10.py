(n, A, B) = list(map(int, input().split()))
arr = []
for x in range(n):
    (i, j) = list(map(int, input().split()))
    arr.append([i, j])
ans = int(0)
i = int(0)
j = int(0)
for i in range(n):
    for j in range(i + 1, n):
        a = arr[i][0]
        b = arr[i][1]
        c = arr[j][0]
        d = arr[j][1]
        temp = a * b + c * d
        if temp <= ans:
            continue
        if b + d <= B and max(a, c) <= A or (max(b, d) <= B and a + c <= A) or (b + c <= B and max(a, d) <= A) or (max(b, c) <= B and a + d <= A) or (a + d <= B and max(c, b) <= A) or (max(a, d) <= B and c + b <= A) or (a + c <= B and max(b, d) <= A) or (max(a, c) <= B and b + d <= A):
            ans = max(ans, temp)
print(ans)
