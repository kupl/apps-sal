T = int(input())
for _ in range(T):
    n = int(input())
    ls = list(map(int, input().split()))
    ans = 'NO'
    for i in range(1, n -1):
        if ls[i] > ls[i-1] and ls[i] > ls[i+1]:
            ans = 'YES'
            break
    if ans == 'NO':
        print(ans)
    else:
        i += 1
        print(ans)
        print(i-1, i, i+1)
