N, M = list(map(int, input().split()))

h = list(map(int, input().split()))
all_dict = {}
for m in range(M):
    a, b = list(map(int, input().split()))
    
    a -= 1
    b -= 1
    
    all_dict.setdefault(a, [])
    all_dict.setdefault(b, [])

    all_dict[a].append(b)
    all_dict[b].append(a)

total_good = 0

for i in range(N):
    is_good = 1
    all_dict.setdefault(i, [])
    for around_h in all_dict[i]:
        if h[around_h] >= h[i]:
            is_good = 0
    total_good += is_good

print(total_good)



