(a, b) = map(int, input().split())
answer = 0
while a >= 1 and b >= 2 or (b >= 1 and a >= 2):
    if a < b:
        a += 1
        b -= 2
        answer += 1
    else:
        b += 1
        a -= 2
        answer += 1
print(answer)
