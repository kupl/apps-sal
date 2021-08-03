n, k = list(map(int, input().split()))
yi = list(map(int, input().split()))
num_peo = 0
for peo in yi:
    if peo <= 5 - k:
        num_peo += 1
print(num_peo // 3)
