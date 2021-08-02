def check(a, k):
    used = [False for i in range(10)]
    while a != 0:
        used[a % 10] = True
        a //= 10
    return sum(used[:k + 1]) == k + 1


n, k = list(map(int, input().split()))
cnt = 0
for i in range(n):
    a = int(input())
    if check(a, k):
        cnt += 1
print(cnt)
