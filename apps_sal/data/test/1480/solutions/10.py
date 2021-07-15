n, k = map(int, input().split())
a = list(map(int, input().split()))
array = [0] * n
for i in range (n):
    array[i] = i + 1
now = 0
for i in range (k):
    dp = (now + a[i] % len(array)) % len(array)
    print(array[dp], end = " ")
    array.pop(dp)
    now = dp
    
