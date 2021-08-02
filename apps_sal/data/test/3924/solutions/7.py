n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
prev = 0;
bags = 0;
for i in range(n):
    if (arr[i] + prev) // k == 0:
        if prev > 0:
            bags += 1;
            prev = 0;
        else:
            prev = arr[i];
    else:
        bags += (arr[i] + prev) // k;
        prev = (arr[i] + prev) % k
if prev != 0:
    bags += 1
print(bags)
