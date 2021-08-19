N = int(input())
H = list(map(int, input().split()))
answer = 0
height = H[0]
for i in H:
    if i >= height:
        answer += 1
    height = max(i, height)
print(answer)
