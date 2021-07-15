n, m = map(int, input().split())
a = list(map(int,input().split())) + [m,0]
left_on = [0] * (n+2)
right_off = [0] * (n+2)

status = 1
for i in range(n+1):
    if status == 1:
        left_on[i] = left_on[i-1] + a[i] - a[i-1]
    else:
        left_on[i] = left_on[i-1]
    status = 1 - status

status = 1 - status
for i in range(n-1,-1,-1):
    if status == 1:
        right_off[i] = right_off[i+1]
    else:
        right_off[i] = right_off[i+1] + a[i+1] - a[i]
    status = 1 - status


ans = left_on[n]

status = 1
for i in range(n+1):
    if a[i] - a[i-1] != 1:
        if status == 1:
            ans = max(ans, left_on[i] - 1 + right_off[i])
        else:
            ans = max(ans, left_on[i] + a[i] - a[i-1] - 1 + right_off[i])
    status = 1 - status 
print(ans)
