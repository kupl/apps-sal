n, k = list(map(int, input().split()))

ls = [1, 0, 0, 0, 0]
ls[2] = n * (n - 1) // 2
ls[3] = n * (n - 1) * (n - 2) // 3
ls[4] = n * (n - 1) * (n - 2) * (n - 3) * 3 // 8 
print(sum(ls[:k + 1]))



