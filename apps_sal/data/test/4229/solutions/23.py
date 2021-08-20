n = int(input())
a = 1
answer = 0
for i in range(n):
    if (a % 3 != 0 and a % 5 != 0) and a % 3 != 0 and (a % 5 != 0):
        answer += a
    a += 1
print(answer)
