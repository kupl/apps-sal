t = int(input())
answers = [0] * t
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arr = [[] for _ in range(n)]
    ans = 0
    for j in range(n):
        pow1 = 0
        cur = a[j]
        while cur % 2 == 0:
            cur //= 2
            pow1 += 1
        arr[j] = [cur, pow1]
    arr.sort(reverse=True)
    cur_nech = -1
    for j in range(n):
        if arr[j][0] != cur_nech:
            ans += arr[j][1]
            cur_nech = arr[j][0]
    answers[i] = ans
print(*answers, sep='\n')

