N, K = map(int, input().split())
friend = list(map(int, input().split()))
clear = []

for i in friend:
    if i >= K:
        clear.append(i)

print(len(clear))
