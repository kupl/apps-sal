

a = 2 ** 5
b = a * "kafjsuhdajsdcbvhsd"

c = "kitten"

F, I, T = map(int, input().split())

likes = [0] * I

for i in range(0, F):
    line = str(input())
    for j in range(0, I):
        if line[j] == 'Y':
            likes[j] += 1

cnt = 0

for l in likes:
    if l >= T:
        cnt += 1

print(cnt)
