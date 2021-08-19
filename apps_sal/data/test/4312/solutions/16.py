(a, b, c, d) = map(int, input().split())
answer = 'No'
while a > 0 and c > 0:
    c -= b
    if c <= 0:
        answer = 'Yes'
    a -= d
print(answer)
