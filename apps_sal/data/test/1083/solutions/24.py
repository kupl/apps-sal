n = int(input())
sm = (n * (n + 1)) // 2
arr = []
tempsm = 0
for i in range(n, 0, -1):
    if(tempsm + i <= (sm + 1) // 2):
        tempsm += i
        arr.append(i)
print(int(abs(2 * sum(arr) - sm)))
print(len(arr))
for i in arr:
    print(i, end=' ')
