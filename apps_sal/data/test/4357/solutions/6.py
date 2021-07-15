num = sorted(list(map(int, input().split())), reverse=True)
print(num[0] * 10 + sum(num[1:]))
