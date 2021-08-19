n = int(input())
a = list(map(int, input().split()))
a = [i for i in a if i > 0]
print(len(set(a)))
