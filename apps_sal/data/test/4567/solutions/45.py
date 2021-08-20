n = int(input())
s = [0] * n
for i in range(n):
    s[i] = int(input())
judge = 0
answer = 0
for i in s:
    answer += i
    if i % 10 == 0:
        judge += 1
s.sort()
mi = 0
for i in s:
    if i % 10 != 0:
        mi = i
        break
if judge == len(s):
    print(0)
else:
    if answer % 10 == 0:
        answer -= mi
    print(answer)
