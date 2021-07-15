N = int(input())
l = list(map(int,input().split()))
l_ans = [[] for _ in range(201)]

for i in range(-100,101):
    sum = 0

    for j in range(N):
        sum = sum + (i-l[j])**2

    l_ans[i+100] = sum

print(min(l_ans))
