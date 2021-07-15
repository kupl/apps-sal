N, A, B = map(int,input().split())

answer = 0

for i in range(N + 1):
    numStrList = list(str(i))
    numIntList = [int(s) for s in numStrList] 

    if A <= sum(numIntList) <= B :
        answer += i

print(answer)
