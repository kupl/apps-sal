def readln():
    return list(map(int, input().rstrip().split()))


n = int(input())
data = list(readln())
rs = max(data) - 25
print(0 if rs < 0 else rs)
