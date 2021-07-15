n, v = map(int, input().strip().split())
answer = 0
n -= 1
if n <= v:
    print(n)
else:
    answer =v

    for i in range(1,n-v + 1):

        answer += (i + 1)
    print(answer)
