num = list(map(int, input().split()))
num = sorted(num)
print(num[0] if num[0] != num[1] else num[2])
