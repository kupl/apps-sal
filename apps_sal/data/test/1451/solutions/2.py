n, k = map(int, input().split())
a = list(map(int, input().split()))

answer = 0
for i in a:
    if str(i).count('7') + str(i).count('4') <= k:
        answer += 1
print(answer)
