(r, c) = list(map(int, input().split()))
last = ''
for i in range(r):
    s = str(input())
    if i == r - 1:
        last = s
answer = 0
left = 0
while left <= c - 1:
    if last[left] == 'B':
        try:
            while last[left] == 'B':
                left += 1
        except Exception:
            pass
        answer += 1
    else:
        left += 1
print(answer)
