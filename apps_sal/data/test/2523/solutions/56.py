S = input()
cnt = [0]
now = '0'
for i in S:
    if now == i:
        cnt[-1] += 1
    else:
        cnt.append(1)
        now = i
ans = len(S)
sum = 0
for i in cnt:
    sum += i
    ans = min(ans, max(sum, len(S) - sum))
print(ans)
