N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

result_score = 10000
result_num = 0

for num, h in enumerate(H, 1):
    temp = T - h * 0.006
    score = abs(A-temp)

    if result_score >= score:
        result_score = score
        result_num = num

print(result_num)
