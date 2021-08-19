abc = list(map(int, input().split()))
k = int(input())
mx = abc.pop(abc.index(max(abc)))
print(mx * pow(2, k) + sum(abc))
