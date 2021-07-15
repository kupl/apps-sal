N = int(input())
T, A = map(int, input().split())
H = map(int, input().split())

result = 0
min_avarage = float('inf')
for i, v in enumerate(H):
    if ((T-v*0.006) - A)**2 < min_avarage:
        min_avarage = ((T-v*0.006) - A)**2
        result = i + 1

print(result)
