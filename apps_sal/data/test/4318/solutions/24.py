# B - Great Ocean View

# 各山頂にあるN個の旅館のうち、海が見える旅館はいくつか

N = int(input())
H = list(map(int, input().split()))

answer = 0
height = H[0]

for i in H:
    if i >= height:
        answer += 1

    height = max(i,height)

print(answer)
