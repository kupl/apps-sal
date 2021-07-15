n = int(input())
s = input()

ans = 0
now_ans = 0
lower = []

for el in s:
    if el.islower():
        if el not in lower:
            lower.append(el)
            now_ans += 1
    else:
        if now_ans > ans:
            ans = now_ans
        lower = []
        now_ans = 0

if now_ans > ans:
    ans = now_ans

print(ans)
