n = int(input())
a = list(map(int, input().split()))
s = sum(a)
answer = []
maxi = max(a)
posMax = a.index(maxi)
for i in range(n):
    if a[i] == maxi and i == posMax:
        tempMax = max(a[:i] + a[i + 1:])
        if s - a[i] - tempMax == tempMax:
            answer.append(i + 1)
    elif s - a[i] - maxi == maxi:
        answer.append(i + 1)
print(len(answer))
print(*answer)
