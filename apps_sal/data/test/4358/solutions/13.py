N = int(input())
list = [int(input()) for i in range(N)]
expensive = max(list)
discount = expensive // 2
total = sum(list) - expensive + discount
print(total)
