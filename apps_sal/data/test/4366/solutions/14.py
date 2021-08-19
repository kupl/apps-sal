(A, B) = list(map(int, input().split()))
answer = A + B
if answer < 24:
    print(answer)
else:
    print(answer - 24)
