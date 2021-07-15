n, m, k = map(int, input().split()) 
k -= 1
print(k // (m + m) + 1, (k % (m + m)) // 2 + 1, 'LR'[k % 2])
