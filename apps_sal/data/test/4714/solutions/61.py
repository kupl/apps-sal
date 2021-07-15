a, b = map(int, input().split())
print(sum(num == num[::-1] for num in map(str,range(a, b+1))))
