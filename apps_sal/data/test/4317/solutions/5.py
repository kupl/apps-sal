

A, B = list(map(int, input().split()))

if (A + B) <= (A - B):
    if (A - B) <= (A * B):
        answer = A * B
    else:
        answer = A - B
elif (A + B) <= (A * B):
    answer = A * B
else:
    answer = A + B

print(answer)
