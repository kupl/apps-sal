(A, B, C, D) = list(map(int, input().split()))
result = 'Yes'
while A > 0 or C > 0:
    C -= B
    A -= D
    if C <= 0:
        break
    elif A <= 0:
        result = 'No'
        break
print(result)
