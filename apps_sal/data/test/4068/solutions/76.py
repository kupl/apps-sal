n, m = map(int, input().split())
a = [0] * (m + 2)
a[m] = n + 10
a[m + 1] = n + 10
for i in range(m):
    a[i] = int(input())
answer = [0] * (n + 1)
answer[0] = 1
if(n == 1):
    if(a[0] == 1):
        print(0)
    else:
        print(1)
else:
    answer[0] = 1
    if(a[0] == 1):
        answer[1] = 0
        a.pop(0)
    else:
        answer[1] = 1
    for i in range(2, n + 1):
        if(a[0] == i or a[1] == i):
            answer[i] = 0
        elif(a[0] == i - 1):
            answer[i] = answer[i - 2]
            a.pop(0)
        else:
            answer[i] = answer[i - 1] + answer[i - 2]
        answer[i] = answer[i] % 1000000007
    print(answer[n])
