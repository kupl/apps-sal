import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
decrement = 0
profit = []
loss = []

for _ in range(n):
    s = input().rstrip()
    min_p = 0
    end_p = 0
    point = 0
    for c in s:
        if c == '(':
            point += 1
        elif c == ')':
            point -= 1
            if point < min_p:
                min_p = point
    else:
        end_p = point
    if 0 <= min_p:
        cnt += end_p
    else:
        if min_p == end_p:
            decrement += end_p
        else:
            if 0 <= end_p:
                profit.append((min_p, end_p))
            else:
                loss.append((min_p, end_p))



profit.sort()
while profit:
    min_p, end_p = profit.pop()
    if cnt+min_p < 0:
        print('No')
        return
    cnt += end_p


loss.sort(reverse=True)
while loss:
    min_p, end_p = loss.pop()
    if cnt+min_p < 0:
        print('No')
        return
    cnt += end_p

print(('Yes' if cnt+decrement == 0 else 'No'))

