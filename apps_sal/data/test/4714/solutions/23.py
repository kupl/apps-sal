(a, b) = map(int, input().split())
answer = 0
for k in range(a, b + 1):
    kk = str(k)
    if kk == kk[::-1]:
        answer += 1
print(answer)
