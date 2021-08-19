(n, k) = map(int, input().split(' '))
arr = sorted([int(i) for i in input().split(' ')])
answer = 0
for i in range(n):
    while 2 * k < arr[i]:
        answer += 1
        k *= 2
    k = max(k, arr[i])
print(answer)
