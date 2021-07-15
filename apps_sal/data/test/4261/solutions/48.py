A, B, C = map(int, input().split())

answer = C - (A - B)

if answer >= 0:
    print(answer)
else:
    print(0)
