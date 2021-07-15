n = int(input())
data = list(map(int, input().split()))
answer = 0
for i in range(n):
    if data.count(data[i]) == 1:
        answer += data[i]
    else:
        while data[i] > 0:
            if data.count(data[i]) == 1:
                answer += data[i]
                break
            else:
                data[i] -= 1
print(answer)
