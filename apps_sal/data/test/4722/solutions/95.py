(a, b) = list(map(int, input().split()))
result = 'ret'
if a % 3 == 0:
    result = 'Possible'
elif b % 3 == 0:
    result = 'Possible'
elif (a + b) % 3 == 0:
    result = 'Possible'
else:
    result = 'Impossible'
print(result)
