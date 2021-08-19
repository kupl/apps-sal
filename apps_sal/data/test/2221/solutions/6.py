In = input().split(' ')
x1 = int(In[0])
y1 = int(In[1])
In = input().split(' ')
x2 = int(In[0])
y2 = int(In[1])
dx = [0]
dy = [0]
n = int(input())
s = input()
for i in range(1, n + 1):
    dx.append(dx[i - 1])
    dy.append(dy[i - 1])
    if s[i - 1] == 'U':
        dy[i] += 1
    elif s[i - 1] == 'D':
        dy[i] -= 1
    elif s[i - 1] == 'R':
        dx[i] += 1
    elif s[i - 1] == 'L':
        dx[i] -= 1
st = 0
en = 10 ** 18 * 2
ans = -1
while st <= en:
    mid = (st + en) // 2
    x = mid // n * dx[n] + dx[mid % n]
    y = mid // n * dy[n] + dy[mid % n]
    newX = x + x1
    newY = y + y1
    need = abs(newX - x2) + abs(newY - y2)
    if mid >= need:
        ans = mid
        en = mid - 1
    else:
        st = mid + 1
print(ans)
