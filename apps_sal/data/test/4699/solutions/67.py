import itertools

N, K = map(int, input().split()) # N円の品物、K個の嫌いな数字
D = set(list(map(int, input().split()))) # 嫌いな数字のリスト
base = set(range(10))

target_num = base - D
keta = len(str(N))

answer = float('inf')
for p in itertools.product(target_num, repeat=keta):
    temp = 0
    for i, num in enumerate(p):
        temp += num * 10**i
        
    if temp >= N:
        answer = min(answer, temp)

for p in itertools.product(target_num, repeat=keta+1):
    temp = 0
    for i, num in enumerate(p):
        temp += num * 10**i
        
    if temp >= N:
        answer = min(answer, temp)

print(answer)
