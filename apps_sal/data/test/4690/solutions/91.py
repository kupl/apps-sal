A, B, C, D = map(int, input().split())

areaAB = A * B
areaCD = C * D

if areaAB == areaCD:
    result = areaAB
elif areaAB > areaCD:
    result = areaAB
else:
    result = areaCD

print(result)
