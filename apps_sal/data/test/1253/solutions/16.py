l = input().split(' ')
n, k = int(l[0]), int(l[1])
l = input().split(' ')
answer = 0
m = 10000
for i in range(0, n):
    a = int(l[i])
    if (a >= 0):
        answer += a
        if a < m:
            m = a
    else:
        if k > 0:
            answer -= a
            k -= 1
        else:
            answer += a
        if -a < m:
            m = -a
if k % 2 == 1:
    answer -= m * 2
print(answer)
