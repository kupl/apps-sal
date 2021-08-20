(A, B) = list(map(int, input().split()))
if A % 3 == 0:
    answer = 'Possible'
elif B % 3 == 0:
    answer = 'Possible'
elif (A + B) % 3 == 0:
    answer = 'Possible'
else:
    answer = 'Impossible'
print(answer)
