abc = list(map(int, input().split()))
k = int(input())
abc.sort()
print(sum(abc[:2], abc[-1] * (2 ** k)))
