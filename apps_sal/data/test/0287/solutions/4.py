n, k = map(int, input().split())
mini, maxi = 0, 0
if n > k and k != 0: 
    mini = 1
else:
    mini = 0

if (n > 3 * k):
    maxi = 2 * k
else:
    maxi = n - k
print(mini, maxi)
