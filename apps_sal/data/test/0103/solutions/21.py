n = int(input())
a = [0] + list(map(int, input().split())) + [1001]
max_ans = 0
ans = 0

for i in range(1, len(a) - 1):
    #print('cur' , a[i])
    if a[i] == a[i - 1] + 1 and a[i] == a[i + 1] - 1:
        ans += 1
        #print('+1')
    else:
        #print(a[i], ans, max_ans)
        #print(max(ans, max_ans))
        max_ans = max(ans, max_ans)
        ans = 0

print(max(max_ans, ans))

