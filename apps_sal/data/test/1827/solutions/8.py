n = int(input())
per = list(map(int, input().split()))
per.sort()
for i in range(n):
    print(per[i], per[-(i + 1)])
