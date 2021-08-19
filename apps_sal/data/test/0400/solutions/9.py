__author__ = 'User'
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
mx = [0] * n
score = 0
for i in range(n):
    if arr[i] != 100:
        mx[i] = (10 - arr[i] % 10, i)
    else:
        mx[i] = (-1, i)
    score += arr[i] // 10
mx.sort()
i = 0
#print(mx, k)
# print(score)
while i < n and k >= mx[i][0]:
    if mx[i][0] != -1:
        k -= mx[i][0]
        arr[mx[i][1]] += mx[i][0]
        score += 1
    i += 1
#print(arr, k)
# print(score)
if i == n:
    i = 0
    k -= k % 10
    while k >= 10 and i < n:
        if arr[i] != 100:
            d = 100 - arr[i]
            if k >= d:
                k -= d
                #arr[i] += d
                #print("d", d)
                score += d // 10
            else:
                #arr[i] += k
                score += k // 10
                k = 0
        i += 1
print(score)
# print(arr)
