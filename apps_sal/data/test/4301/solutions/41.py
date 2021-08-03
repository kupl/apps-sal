n = int(input())
arr = [int(input()) for _ in range(n)]
ar = sorted(arr)
mx = ar[-1]
sc = ar[-2]

for ele in arr:
    if ele == mx:
        print(sc)
    else:
        print(mx)
