n = int(input())
a = list(map(int, input().split()))
l = [0] * n
for x in a:
    l[x] += 1
for i in range(n):
    if l[i] > 2:
        print(0)
        return
    if l[i] > 0 and (i + n) % 2 == 0: 
        print(0)
        return
if n % 2 == 1 and l[0] > 1:
    print(0)
    return
print(pow(2, n // 2, 10 ** 9 + 7))
