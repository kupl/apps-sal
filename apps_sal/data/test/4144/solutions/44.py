n = int(input())

answer = (10 ** n) - (9 ** n) - (9 ** n) + (8 ** n)
    
answer = answer % (10 ** 9 + 7)
print(answer)
