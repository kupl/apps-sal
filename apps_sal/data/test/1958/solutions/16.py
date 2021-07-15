n, k = map(int, input().split())
answer = [0] * n
for i in range(n):
    per = input()
    answer[-(i+1)] =  1 if per == 'halfplus' else 0
per = 0
ans = 0
for i in range(0, n):
    if answer[i] == 1:
        ans += (per * k) + (k//2)
        per = per*2 + 1
    else:
        ans += (per * k)
        per = per * 2
print(ans)
