n = int(input())
a = list(map(int, input().split()))
(max, fee) = list(map(int, input().split()))
total = 0
a.sort(reverse=True)
for i in range(n):
    if a[i] > max:
        num = -(-(a[i] - max) // (max + fee))
        total = total + fee * num
    else:
        break
print(total)
