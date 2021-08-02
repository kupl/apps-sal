l, r = list(map(int, input().split()))
answer = "-1"
for i in range(l, r + 1):
    s = str(i)
    digits = set(list(s))
    if len(s) == len(digits):
        answer = s
        break
print(answer)
