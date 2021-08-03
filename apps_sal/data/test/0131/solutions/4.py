n = int(input())
a = [int(v) for v in input().split()]
b = [int(v) for v in input().split()]

print(["No", "Yes"][sum(a) >= sum(b)])
