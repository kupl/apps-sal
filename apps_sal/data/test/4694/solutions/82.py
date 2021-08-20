n = int(input())
street = sorted(list(map(int, input().split())))
print(street[-1] - street[0])
