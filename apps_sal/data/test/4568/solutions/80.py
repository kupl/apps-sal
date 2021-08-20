n = int(input())
s = input()
alh = 'abcdefghijklmnopqrstuvwxyz'
max = 0
for i in range(n):
    front = s[:i]
    rear = s[i:]
    cnt = 0
    for j in alh:
        if j in front and j in rear:
            cnt += 1
    if cnt > max:
        max = cnt
print(max)
