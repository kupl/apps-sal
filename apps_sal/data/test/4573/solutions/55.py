n = int(input())
x = list(map(int, input().split()))
l = sorted(x)
ans_1 = l[n // 2 - 1]
ans_2 = l[n // 2]
for i in x:
    if i <= ans_1:
        print(ans_2)
    else:
        print(ans_1)
