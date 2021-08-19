input()
w = list(map(int, input().split()))
b = list(map(int, input().split()))
a = []
ans = 0
for x in b:
    x -= 1
    cur_sum = 0
    for (i, num) in enumerate(a):
        if num == x:
            a = [num] + a[:i] + a[i + 1:]
            break
        cur_sum += w[num]
    else:
        a = [x] + a
    ans += cur_sum
print(ans)
